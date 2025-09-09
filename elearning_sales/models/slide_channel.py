from odoo import models, fields, api




class SlideChannel(models.Model):
    _inherit = 'slide.channel'


    product_template_id = fields.Many2one(
        'product.template',
        string="Product",
        domain="[('is_course_access', '=', True), ('type', '=', 'service')]"
    )
    display_price = fields.Float(related="product_template_id.list_price")
    display_price_formated = fields.Char(compute="_compute_display_price_formated")

    sales_total = fields.Float(compute="_compute_sales_total", store=True)
    sales_total_formated = fields.Char(compute="_compute_sales_total_formated")

    sales_count = fields.Integer(compute="_compute_sales_count", store=True)

    def _compute_display_price_formated(self):
        for rec in self:
            rec.display_price_formated = str(rec.display_price) + ' ' + rec.env.company.currency_id.symbol

    @api.depends('product_template_id')
    def _compute_sales_total(self):
        for rec in self:
            rec.sales_total = 0.0
            if rec.product_template_id:

                order_lines = rec.env['sale.order.line'].search([
                    ('product_template_id', '=', rec.product_template_id.id),
                    ('order_id.state', 'in', ['sale', 'done'])  # Only count confirmed orders
                ])
                    
                rec.sales_total = sum(line.price_subtotal for line in order_lines)
                print('33333333333333333333333333333333333333333333333', rec.sales_total)
    
    def recompute_sales_total(self):
        for rec in self:
            rec._compute_sales_total()

    def _compute_sales_total_formated(self):
        for rec in self:
            currency = rec.env.company.currency_id.symbol
            rec._compute_sales_total()
            rec._compute_sales_count()
            total = rec.sales_total

            # Format with space as thousands separator
            total_str = f"{total:,.2f}"  # Example: 1,234,567.89
            rec.sales_total_formated = f"{total_str} {currency}"
    
    @api.depends('product_template_id')
    def _compute_sales_count(self):
        for rec in self:
            rec.sales_count = 0
            if rec.product_template_id:

                rec.sales_count = rec.env['sale.order.line'].search_count([
                    ('product_template_id', '=', rec.product_template_id.id),
                    ('order_id.state', 'in', ['sale', 'done'])  # Only count confirmed orders
                ])
                print('33333333333333333333333333333333333333333333333', rec.sales_count)
    
    def recompute_sales_count(self):
        for rec in self:
            rec._compute_sales_count()
    
    def action_view_sales_order(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': f'Sales Orders - {self.product_template_id.name}',
            'res_model': 'sale.order',
            'view_mode': 'list,form',
            'target': 'current',
            'domain': [('order_line.product_template_id', '=', self.product_template_id.id)],
            'context': {
                'search_default_filter_sale': 1,
                'search_default_filter_done': 1,
            }
        }
    
    