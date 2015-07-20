(function() {
    var instance = openerp;
    var _t = instance.web._t,
        _lt = instance.web._lt;
    var QWeb = instance.web.qweb;

    instance.web.form.FieldPercentage = instance.web.form.FieldFloat.extend({
        template: "FieldPercentage",
        widget_class: 'oe_form_field_float oe_form_field_monetary',
        init: function() {
            this._super.apply(this, arguments);
            if (!this.options.position) {
                this.set({"percentage_position": 'after'});
            } else {
                this.set({"percentage_position": this.options.position});
            };
            this.get_symbol();
        },
        start: function() {
            return this._super();
        },
        get_symbol: function() {
            var self = this;
            self.set({"percentage_symbol": '%'});
        },
        parse_value: function(val, def) {
            return instance.web.parse_value(val, {type: "float", digits: (this.node.attrs || {}).digits || this.field.digits}, def);
        },
        format_value: function(val, def) {
            return instance.web.format_value(val, {type: "float", digits: (this.node.attrs || {}).digits || this.field.digits}, def);
        },
    });

    instance.web.form.widgets.add('percentage', 'instance.web.form.FieldPercentage');
})();
