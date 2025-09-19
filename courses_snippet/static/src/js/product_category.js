/** @odoo-module */
import { renderToElement } from "@web/core/utils/render";
import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";



publicWidget.registry.get_product_tab = publicWidget.Widget.extend({
    selector : '.featured_courses_section',
    async willStart() {
        const result = await rpc('/get_featured_courses', {});
        if(result){
            this.$target.empty().html(renderToElement('courses_snippet.courses_data', {result: result}))
        }
    },
});
