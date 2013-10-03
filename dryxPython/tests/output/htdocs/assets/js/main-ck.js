/*!
 * jQuery JavaScript Library v1.10.1
 * http://jquery.com/
 *
 * Includes Sizzle.js
 * http://sizzlejs.com/
 *
 * Copyright 2005, 2013 jQuery Foundation, Inc. and other contributors
 * Released under the MIT license
 * http://jquery.org/license
 *
 * Date: 2013-05-30T21:49Z
 */(function(e, t) {
    function H(e) {
        var t = e.length, n = w.type(e);
        return w.isWindow(e) ? !1 : e.nodeType === 1 && t ? !0 : n === "array" || n !== "function" && (t === 0 || typeof t == "number" && t > 0 && t - 1 in e);
    }
    function j(e) {
        var t = B[e] = {};
        w.each(e.match(S) || [], function(e, n) {
            t[n] = !0;
        });
        return t;
    }
    function q(e, n, r, i) {
        if (!w.acceptData(e)) return;
        var s, o, u = w.expando, a = e.nodeType, f = a ? w.cache : e, l = a ? e[u] : e[u] && u;
        if ((!l || !f[l] || !i && !f[l].data) && r === t && typeof n == "string") return;
        l || (a ? l = e[u] = c.pop() || w.guid++ : l = u);
        f[l] || (f[l] = a ? {} : {
            toJSON: w.noop
        });
        if (typeof n == "object" || typeof n == "function") i ? f[l] = w.extend(f[l], n) : f[l].data = w.extend(f[l].data, n);
        o = f[l];
        if (!i) {
            o.data || (o.data = {});
            o = o.data;
        }
        r !== t && (o[w.camelCase(n)] = r);
        if (typeof n == "string") {
            s = o[n];
            s == null && (s = o[w.camelCase(n)]);
        } else s = o;
        return s;
    }
    function R(e, t, n) {
        if (!w.acceptData(e)) return;
        var r, i, s = e.nodeType, o = s ? w.cache : e, u = s ? e[w.expando] : w.expando;
        if (!o[u]) return;
        if (t) {
            r = n ? o[u] : o[u].data;
            if (r) {
                if (!w.isArray(t)) if (t in r) t = [ t ]; else {
                    t = w.camelCase(t);
                    t in r ? t = [ t ] : t = t.split(" ");
                } else t = t.concat(w.map(t, w.camelCase));
                i = t.length;
                while (i--) delete r[t[i]];
                if (n ? !z(r) : !w.isEmptyObject(r)) return;
            }
        }
        if (!n) {
            delete o[u].data;
            if (!z(o[u])) return;
        }
        s ? w.cleanData([ e ], !0) : w.support.deleteExpando || o != o.window ? delete o[u] : o[u] = null;
    }
    function U(e, n, r) {
        if (r === t && e.nodeType === 1) {
            var i = "data-" + n.replace(I, "-$1").toLowerCase();
            r = e.getAttribute(i);
            if (typeof r == "string") {
                try {
                    r = r === "true" ? !0 : r === "false" ? !1 : r === "null" ? null : +r + "" === r ? +r : F.test(r) ? w.parseJSON(r) : r;
                } catch (s) {}
                w.data(e, n, r);
            } else r = t;
        }
        return r;
    }
    function z(e) {
        var t;
        for (t in e) {
            if (t === "data" && w.isEmptyObject(e[t])) continue;
            if (t !== "toJSON") return !1;
        }
        return !0;
    }
    function it() {
        return !0;
    }
    function st() {
        return !1;
    }
    function ot() {
        try {
            return o.activeElement;
        } catch (e) {}
    }
    function ct(e, t) {
        do e = e[t]; while (e && e.nodeType !== 1);
        return e;
    }
    function ht(e, t, n) {
        if (w.isFunction(t)) return w.grep(e, function(e, r) {
            return !!t.call(e, r, e) !== n;
        });
        if (t.nodeType) return w.grep(e, function(e) {
            return e === t !== n;
        });
        if (typeof t == "string") {
            if (ut.test(t)) return w.filter(t, e, n);
            t = w.filter(t, e);
        }
        return w.grep(e, function(e) {
            return w.inArray(e, t) >= 0 !== n;
        });
    }
    function pt(e) {
        var t = dt.split("|"), n = e.createDocumentFragment();
        if (n.createElement) while (t.length) n.createElement(t.pop());
        return n;
    }
    function Mt(e, t) {
        return w.nodeName(e, "table") && w.nodeName(t.nodeType === 1 ? t : t.firstChild, "tr") ? e.getElementsByTagName("tbody")[0] || e.appendChild(e.ownerDocument.createElement("tbody")) : e;
    }
    function _t(e) {
        e.type = (w.find.attr(e, "type") !== null) + "/" + e.type;
        return e;
    }
    function Dt(e) {
        var t = Ct.exec(e.type);
        t ? e.type = t[1] : e.removeAttribute("type");
        return e;
    }
    function Pt(e, t) {
        var n, r = 0;
        for (; (n = e[r]) != null; r++) w._data(n, "globalEval", !t || w._data(t[r], "globalEval"));
    }
    function Ht(e, t) {
        if (t.nodeType !== 1 || !w.hasData(e)) return;
        var n, r, i, s = w._data(e), o = w._data(t, s), u = s.events;
        if (u) {
            delete o.handle;
            o.events = {};
            for (n in u) for (r = 0, i = u[n].length; r < i; r++) w.event.add(t, n, u[n][r]);
        }
        o.data && (o.data = w.extend({}, o.data));
    }
    function Bt(e, t) {
        var n, r, i;
        if (t.nodeType !== 1) return;
        n = t.nodeName.toLowerCase();
        if (!w.support.noCloneEvent && t[w.expando]) {
            i = w._data(t);
            for (r in i.events) w.removeEvent(t, r, i.handle);
            t.removeAttribute(w.expando);
        }
        if (n === "script" && t.text !== e.text) {
            _t(t).text = e.text;
            Dt(t);
        } else if (n === "object") {
            t.parentNode && (t.outerHTML = e.outerHTML);
            w.support.html5Clone && e.innerHTML && !w.trim(t.innerHTML) && (t.innerHTML = e.innerHTML);
        } else if (n === "input" && xt.test(e.type)) {
            t.defaultChecked = t.checked = e.checked;
            t.value !== e.value && (t.value = e.value);
        } else if (n === "option") t.defaultSelected = t.selected = e.defaultSelected; else if (n === "input" || n === "textarea") t.defaultValue = e.defaultValue;
    }
    function jt(e, n) {
        var r, s, o = 0, u = typeof e.getElementsByTagName !== i ? e.getElementsByTagName(n || "*") : typeof e.querySelectorAll !== i ? e.querySelectorAll(n || "*") : t;
        if (!u) for (u = [], r = e.childNodes || e; (s = r[o]) != null; o++) !n || w.nodeName(s, n) ? u.push(s) : w.merge(u, jt(s, n));
        return n === t || n && w.nodeName(e, n) ? w.merge([ e ], u) : u;
    }
    function Ft(e) {
        xt.test(e.type) && (e.defaultChecked = e.checked);
    }
    function tn(e, t) {
        if (t in e) return t;
        var n = t.charAt(0).toUpperCase() + t.slice(1), r = t, i = en.length;
        while (i--) {
            t = en[i] + n;
            if (t in e) return t;
        }
        return r;
    }
    function nn(e, t) {
        e = t || e;
        return w.css(e, "display") === "none" || !w.contains(e.ownerDocument, e);
    }
    function rn(e, t) {
        var n, r, i, s = [], o = 0, u = e.length;
        for (; o < u; o++) {
            r = e[o];
            if (!r.style) continue;
            s[o] = w._data(r, "olddisplay");
            n = r.style.display;
            if (t) {
                !s[o] && n === "none" && (r.style.display = "");
                r.style.display === "" && nn(r) && (s[o] = w._data(r, "olddisplay", an(r.nodeName)));
            } else if (!s[o]) {
                i = nn(r);
                (n && n !== "none" || !i) && w._data(r, "olddisplay", i ? n : w.css(r, "display"));
            }
        }
        for (o = 0; o < u; o++) {
            r = e[o];
            if (!r.style) continue;
            if (!t || r.style.display === "none" || r.style.display === "") r.style.display = t ? s[o] || "" : "none";
        }
        return e;
    }
    function sn(e, t, n) {
        var r = $t.exec(t);
        return r ? Math.max(0, r[1] - (n || 0)) + (r[2] || "px") : t;
    }
    function on(e, t, n, r, i) {
        var s = n === (r ? "border" : "content") ? 4 : t === "width" ? 1 : 0, o = 0;
        for (; s < 4; s += 2) {
            n === "margin" && (o += w.css(e, n + Zt[s], !0, i));
            if (r) {
                n === "content" && (o -= w.css(e, "padding" + Zt[s], !0, i));
                n !== "margin" && (o -= w.css(e, "border" + Zt[s] + "Width", !0, i));
            } else {
                o += w.css(e, "padding" + Zt[s], !0, i);
                n !== "padding" && (o += w.css(e, "border" + Zt[s] + "Width", !0, i));
            }
        }
        return o;
    }
    function un(e, t, n) {
        var r = !0, i = t === "width" ? e.offsetWidth : e.offsetHeight, s = qt(e), o = w.support.boxSizing && w.css(e, "boxSizing", !1, s) === "border-box";
        if (i <= 0 || i == null) {
            i = Rt(e, t, s);
            if (i < 0 || i == null) i = e.style[t];
            if (Jt.test(i)) return i;
            r = o && (w.support.boxSizingReliable || i === e.style[t]);
            i = parseFloat(i) || 0;
        }
        return i + on(e, t, n || (o ? "border" : "content"), r, s) + "px";
    }
    function an(e) {
        var t = o, n = Qt[e];
        if (!n) {
            n = fn(e, t);
            if (n === "none" || !n) {
                It = (It || w("<iframe frameborder='0' width='0' height='0'/>").css("cssText", "display:block !important")).appendTo(t.documentElement);
                t = (It[0].contentWindow || It[0].contentDocument).document;
                t.write("<!doctype html><html><body>");
                t.close();
                n = fn(e, t);
                It.detach();
            }
            Qt[e] = n;
        }
        return n;
    }
    function fn(e, t) {
        var n = w(t.createElement(e)).appendTo(t.body), r = w.css(n[0], "display");
        n.remove();
        return r;
    }
    function vn(e, t, n, r) {
        var i;
        if (w.isArray(t)) w.each(t, function(t, i) {
            n || cn.test(e) ? r(e, i) : vn(e + "[" + (typeof i == "object" ? t : "") + "]", i, n, r);
        }); else if (!n && w.type(t) === "object") for (i in t) vn(e + "[" + i + "]", t[i], n, r); else r(e, t);
    }
    function _n(e) {
        return function(t, n) {
            if (typeof t != "string") {
                n = t;
                t = "*";
            }
            var r, i = 0, s = t.toLowerCase().match(S) || [];
            if (w.isFunction(n)) while (r = s[i++]) if (r[0] === "+") {
                r = r.slice(1) || "*";
                (e[r] = e[r] || []).unshift(n);
            } else (e[r] = e[r] || []).push(n);
        };
    }
    function Dn(e, t, n, r) {
        function o(u) {
            var a;
            i[u] = !0;
            w.each(e[u] || [], function(e, u) {
                var f = u(t, n, r);
                if (typeof f == "string" && !s && !i[f]) {
                    t.dataTypes.unshift(f);
                    o(f);
                    return !1;
                }
                if (s) return !(a = f);
            });
            return a;
        }
        var i = {}, s = e === An;
        return o(t.dataTypes[0]) || !i["*"] && o("*");
    }
    function Pn(e, n) {
        var r, i, s = w.ajaxSettings.flatOptions || {};
        for (i in n) n[i] !== t && ((s[i] ? e : r || (r = {}))[i] = n[i]);
        r && w.extend(!0, e, r);
        return e;
    }
    function Hn(e, n, r) {
        var i, s, o, u, a = e.contents, f = e.dataTypes;
        while (f[0] === "*") {
            f.shift();
            s === t && (s = e.mimeType || n.getResponseHeader("Content-Type"));
        }
        if (s) for (u in a) if (a[u] && a[u].test(s)) {
            f.unshift(u);
            break;
        }
        if (f[0] in r) o = f[0]; else {
            for (u in r) {
                if (!f[0] || e.converters[u + " " + f[0]]) {
                    o = u;
                    break;
                }
                i || (i = u);
            }
            o = o || i;
        }
        if (o) {
            o !== f[0] && f.unshift(o);
            return r[o];
        }
    }
    function Bn(e, t, n, r) {
        var i, s, o, u, a, f = {}, l = e.dataTypes.slice();
        if (l[1]) for (o in e.converters) f[o.toLowerCase()] = e.converters[o];
        s = l.shift();
        while (s) {
            e.responseFields[s] && (n[e.responseFields[s]] = t);
            !a && r && e.dataFilter && (t = e.dataFilter(t, e.dataType));
            a = s;
            s = l.shift();
            if (s) if (s === "*") s = a; else if (a !== "*" && a !== s) {
                o = f[a + " " + s] || f["* " + s];
                if (!o) for (i in f) {
                    u = i.split(" ");
                    if (u[1] === s) {
                        o = f[a + " " + u[0]] || f["* " + u[0]];
                        if (o) {
                            if (o === !0) o = f[i]; else if (f[i] !== !0) {
                                s = u[0];
                                l.unshift(u[1]);
                            }
                            break;
                        }
                    }
                }
                if (o !== !0) if (o && e["throws"]) t = o(t); else try {
                    t = o(t);
                } catch (c) {
                    return {
                        state: "parsererror",
                        error: o ? c : "No conversion from " + a + " to " + s
                    };
                }
            }
        }
        return {
            state: "success",
            data: t
        };
    }
    function zn() {
        try {
            return new e.XMLHttpRequest;
        } catch (t) {}
    }
    function Wn() {
        try {
            return new e.ActiveXObject("Microsoft.XMLHTTP");
        } catch (t) {}
    }
    function Yn() {
        setTimeout(function() {
            Xn = t;
        });
        return Xn = w.now();
    }
    function Zn(e, t, n) {
        var r, i = (Gn[t] || []).concat(Gn["*"]), s = 0, o = i.length;
        for (; s < o; s++) if (r = i[s].call(n, t, e)) return r;
    }
    function er(e, t, n) {
        var r, i, s = 0, o = Qn.length, u = w.Deferred().always(function() {
            delete a.elem;
        }), a = function() {
            if (i) return !1;
            var t = Xn || Yn(), n = Math.max(0, f.startTime + f.duration - t), r = n / f.duration || 0, s = 1 - r, o = 0, a = f.tweens.length;
            for (; o < a; o++) f.tweens[o].run(s);
            u.notifyWith(e, [ f, s, n ]);
            if (s < 1 && a) return n;
            u.resolveWith(e, [ f ]);
            return !1;
        }, f = u.promise({
            elem: e,
            props: w.extend({}, t),
            opts: w.extend(!0, {
                specialEasing: {}
            }, n),
            originalProperties: t,
            originalOptions: n,
            startTime: Xn || Yn(),
            duration: n.duration,
            tweens: [],
            createTween: function(t, n) {
                var r = w.Tween(e, f.opts, t, n, f.opts.specialEasing[t] || f.opts.easing);
                f.tweens.push(r);
                return r;
            },
            stop: function(t) {
                var n = 0, r = t ? f.tweens.length : 0;
                if (i) return this;
                i = !0;
                for (; n < r; n++) f.tweens[n].run(1);
                t ? u.resolveWith(e, [ f, t ]) : u.rejectWith(e, [ f, t ]);
                return this;
            }
        }), l = f.props;
        tr(l, f.opts.specialEasing);
        for (; s < o; s++) {
            r = Qn[s].call(f, e, l, f.opts);
            if (r) return r;
        }
        w.map(l, Zn, f);
        w.isFunction(f.opts.start) && f.opts.start.call(e, f);
        w.fx.timer(w.extend(a, {
            elem: e,
            anim: f,
            queue: f.opts.queue
        }));
        return f.progress(f.opts.progress).done(f.opts.done, f.opts.complete).fail(f.opts.fail).always(f.opts.always);
    }
    function tr(e, t) {
        var n, r, i, s, o;
        for (n in e) {
            r = w.camelCase(n);
            i = t[r];
            s = e[n];
            if (w.isArray(s)) {
                i = s[1];
                s = e[n] = s[0];
            }
            if (n !== r) {
                e[r] = s;
                delete e[n];
            }
            o = w.cssHooks[r];
            if (o && "expand" in o) {
                s = o.expand(s);
                delete e[r];
                for (n in s) if (!(n in e)) {
                    e[n] = s[n];
                    t[n] = i;
                }
            } else t[r] = i;
        }
    }
    function nr(e, t, n) {
        var r, i, s, o, u, a, f = this, l = {}, c = e.style, h = e.nodeType && nn(e), p = w._data(e, "fxshow");
        if (!n.queue) {
            u = w._queueHooks(e, "fx");
            if (u.unqueued == null) {
                u.unqueued = 0;
                a = u.empty.fire;
                u.empty.fire = function() {
                    u.unqueued || a();
                };
            }
            u.unqueued++;
            f.always(function() {
                f.always(function() {
                    u.unqueued--;
                    w.queue(e, "fx").length || u.empty.fire();
                });
            });
        }
        if (e.nodeType === 1 && ("height" in t || "width" in t)) {
            n.overflow = [ c.overflow, c.overflowX, c.overflowY ];
            w.css(e, "display") === "inline" && w.css(e, "float") === "none" && (!w.support.inlineBlockNeedsLayout || an(e.nodeName) === "inline" ? c.display = "inline-block" : c.zoom = 1);
        }
        if (n.overflow) {
            c.overflow = "hidden";
            w.support.shrinkWrapBlocks || f.always(function() {
                c.overflow = n.overflow[0];
                c.overflowX = n.overflow[1];
                c.overflowY = n.overflow[2];
            });
        }
        for (r in t) {
            i = t[r];
            if ($n.exec(i)) {
                delete t[r];
                s = s || i === "toggle";
                if (i === (h ? "hide" : "show")) continue;
                l[r] = p && p[r] || w.style(e, r);
            }
        }
        if (!w.isEmptyObject(l)) {
            p ? "hidden" in p && (h = p.hidden) : p = w._data(e, "fxshow", {});
            s && (p.hidden = !h);
            h ? w(e).show() : f.done(function() {
                w(e).hide();
            });
            f.done(function() {
                var t;
                w._removeData(e, "fxshow");
                for (t in l) w.style(e, t, l[t]);
            });
            for (r in l) {
                o = Zn(h ? p[r] : 0, r, f);
                if (!(r in p)) {
                    p[r] = o.start;
                    if (h) {
                        o.end = o.start;
                        o.start = r === "width" || r === "height" ? 1 : 0;
                    }
                }
            }
        }
    }
    function rr(e, t, n, r, i) {
        return new rr.prototype.init(e, t, n, r, i);
    }
    function ir(e, t) {
        var n, r = {
            height: e
        }, i = 0;
        t = t ? 1 : 0;
        for (; i < 4; i += 2 - t) {
            n = Zt[i];
            r["margin" + n] = r["padding" + n] = e;
        }
        t && (r.opacity = r.width = e);
        return r;
    }
    function sr(e) {
        return w.isWindow(e) ? e : e.nodeType === 9 ? e.defaultView || e.parentWindow : !1;
    }
    var n, r, i = typeof t, s = e.location, o = e.document, u = o.documentElement, a = e.jQuery, f = e.$, l = {}, c = [], h = "1.10.1", p = c.concat, d = c.push, v = c.slice, m = c.indexOf, g = l.toString, y = l.hasOwnProperty, b = h.trim, w = function(e, t) {
        return new w.fn.init(e, t, r);
    }, E = /[+-]?(?:\d*\.|)\d+(?:[eE][+-]?\d+|)/.source, S = /\S+/g, x = /^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g, T = /^(?:\s*(<[\w\W]+>)[^>]*|#([\w-]*))$/, N = /^<(\w+)\s*\/?>(?:<\/\1>|)$/, C = /^[\],:{}\s]*$/, k = /(?:^|:|,)(?:\s*\[)+/g, L = /\\(?:["\\\/bfnrt]|u[\da-fA-F]{4})/g, A = /"[^"\\\r\n]*"|true|false|null|-?(?:\d+\.|)\d+(?:[eE][+-]?\d+|)/g, O = /^-ms-/, M = /-([\da-z])/gi, _ = function(e, t) {
        return t.toUpperCase();
    }, D = function(e) {
        if (o.addEventListener || e.type === "load" || o.readyState === "complete") {
            P();
            w.ready();
        }
    }, P = function() {
        if (o.addEventListener) {
            o.removeEventListener("DOMContentLoaded", D, !1);
            e.removeEventListener("load", D, !1);
        } else {
            o.detachEvent("onreadystatechange", D);
            e.detachEvent("onload", D);
        }
    };
    w.fn = w.prototype = {
        jquery: h,
        constructor: w,
        init: function(e, n, r) {
            var i, s;
            if (!e) return this;
            if (typeof e == "string") {
                e.charAt(0) === "<" && e.charAt(e.length - 1) === ">" && e.length >= 3 ? i = [ null, e, null ] : i = T.exec(e);
                if (i && (i[1] || !n)) {
                    if (i[1]) {
                        n = n instanceof w ? n[0] : n;
                        w.merge(this, w.parseHTML(i[1], n && n.nodeType ? n.ownerDocument || n : o, !0));
                        if (N.test(i[1]) && w.isPlainObject(n)) for (i in n) w.isFunction(this[i]) ? this[i](n[i]) : this.attr(i, n[i]);
                        return this;
                    }
                    s = o.getElementById(i[2]);
                    if (s && s.parentNode) {
                        if (s.id !== i[2]) return r.find(e);
                        this.length = 1;
                        this[0] = s;
                    }
                    this.context = o;
                    this.selector = e;
                    return this;
                }
                return !n || n.jquery ? (n || r).find(e) : this.constructor(n).find(e);
            }
            if (e.nodeType) {
                this.context = this[0] = e;
                this.length = 1;
                return this;
            }
            if (w.isFunction(e)) return r.ready(e);
            if (e.selector !== t) {
                this.selector = e.selector;
                this.context = e.context;
            }
            return w.makeArray(e, this);
        },
        selector: "",
        length: 0,
        toArray: function() {
            return v.call(this);
        },
        get: function(e) {
            return e == null ? this.toArray() : e < 0 ? this[this.length + e] : this[e];
        },
        pushStack: function(e) {
            var t = w.merge(this.constructor(), e);
            t.prevObject = this;
            t.context = this.context;
            return t;
        },
        each: function(e, t) {
            return w.each(this, e, t);
        },
        ready: function(e) {
            w.ready.promise().done(e);
            return this;
        },
        slice: function() {
            return this.pushStack(v.apply(this, arguments));
        },
        first: function() {
            return this.eq(0);
        },
        last: function() {
            return this.eq(-1);
        },
        eq: function(e) {
            var t = this.length, n = +e + (e < 0 ? t : 0);
            return this.pushStack(n >= 0 && n < t ? [ this[n] ] : []);
        },
        map: function(e) {
            return this.pushStack(w.map(this, function(t, n) {
                return e.call(t, n, t);
            }));
        },
        end: function() {
            return this.prevObject || this.constructor(null);
        },
        push: d,
        sort: [].sort,
        splice: [].splice
    };
    w.fn.init.prototype = w.fn;
    w.extend = w.fn.extend = function() {
        var e, n, r, i, s, o, u = arguments[0] || {}, a = 1, f = arguments.length, l = !1;
        if (typeof u == "boolean") {
            l = u;
            u = arguments[1] || {};
            a = 2;
        }
        typeof u != "object" && !w.isFunction(u) && (u = {});
        if (f === a) {
            u = this;
            --a;
        }
        for (; a < f; a++) if ((s = arguments[a]) != null) for (i in s) {
            e = u[i];
            r = s[i];
            if (u === r) continue;
            if (l && r && (w.isPlainObject(r) || (n = w.isArray(r)))) {
                if (n) {
                    n = !1;
                    o = e && w.isArray(e) ? e : [];
                } else o = e && w.isPlainObject(e) ? e : {};
                u[i] = w.extend(l, o, r);
            } else r !== t && (u[i] = r);
        }
        return u;
    };
    w.extend({
        expando: "jQuery" + (h + Math.random()).replace(/\D/g, ""),
        noConflict: function(t) {
            e.$ === w && (e.$ = f);
            t && e.jQuery === w && (e.jQuery = a);
            return w;
        },
        isReady: !1,
        readyWait: 1,
        holdReady: function(e) {
            e ? w.readyWait++ : w.ready(!0);
        },
        ready: function(e) {
            if (e === !0 ? --w.readyWait : w.isReady) return;
            if (!o.body) return setTimeout(w.ready);
            w.isReady = !0;
            if (e !== !0 && --w.readyWait > 0) return;
            n.resolveWith(o, [ w ]);
            w.fn.trigger && w(o).trigger("ready").off("ready");
        },
        isFunction: function(e) {
            return w.type(e) === "function";
        },
        isArray: Array.isArray || function(e) {
            return w.type(e) === "array";
        },
        isWindow: function(e) {
            return e != null && e == e.window;
        },
        isNumeric: function(e) {
            return !isNaN(parseFloat(e)) && isFinite(e);
        },
        type: function(e) {
            return e == null ? String(e) : typeof e == "object" || typeof e == "function" ? l[g.call(e)] || "object" : typeof e;
        },
        isPlainObject: function(e) {
            var n;
            if (!e || w.type(e) !== "object" || e.nodeType || w.isWindow(e)) return !1;
            try {
                if (e.constructor && !y.call(e, "constructor") && !y.call(e.constructor.prototype, "isPrototypeOf")) return !1;
            } catch (r) {
                return !1;
            }
            if (w.support.ownLast) for (n in e) return y.call(e, n);
            for (n in e) ;
            return n === t || y.call(e, n);
        },
        isEmptyObject: function(e) {
            var t;
            for (t in e) return !1;
            return !0;
        },
        error: function(e) {
            throw new Error(e);
        },
        parseHTML: function(e, t, n) {
            if (!e || typeof e != "string") return null;
            if (typeof t == "boolean") {
                n = t;
                t = !1;
            }
            t = t || o;
            var r = N.exec(e), i = !n && [];
            if (r) return [ t.createElement(r[1]) ];
            r = w.buildFragment([ e ], t, i);
            i && w(i).remove();
            return w.merge([], r.childNodes);
        },
        parseJSON: function(t) {
            if (e.JSON && e.JSON.parse) return e.JSON.parse(t);
            if (t === null) return t;
            if (typeof t == "string") {
                t = w.trim(t);
                if (t && C.test(t.replace(L, "@").replace(A, "]").replace(k, ""))) return (new Function("return " + t))();
            }
            w.error("Invalid JSON: " + t);
        },
        parseXML: function(n) {
            var r, i;
            if (!n || typeof n != "string") return null;
            try {
                if (e.DOMParser) {
                    i = new DOMParser;
                    r = i.parseFromString(n, "text/xml");
                } else {
                    r = new ActiveXObject("Microsoft.XMLDOM");
                    r.async = "false";
                    r.loadXML(n);
                }
            } catch (s) {
                r = t;
            }
            (!r || !r.documentElement || r.getElementsByTagName("parsererror").length) && w.error("Invalid XML: " + n);
            return r;
        },
        noop: function() {},
        globalEval: function(t) {
            t && w.trim(t) && (e.execScript || function(t) {
                e.eval.call(e, t);
            })(t);
        },
        camelCase: function(e) {
            return e.replace(O, "ms-").replace(M, _);
        },
        nodeName: function(e, t) {
            return e.nodeName && e.nodeName.toLowerCase() === t.toLowerCase();
        },
        each: function(e, t, n) {
            var r, i = 0, s = e.length, o = H(e);
            if (n) if (o) for (; i < s; i++) {
                r = t.apply(e[i], n);
                if (r === !1) break;
            } else for (i in e) {
                r = t.apply(e[i], n);
                if (r === !1) break;
            } else if (o) for (; i < s; i++) {
                r = t.call(e[i], i, e[i]);
                if (r === !1) break;
            } else for (i in e) {
                r = t.call(e[i], i, e[i]);
                if (r === !1) break;
            }
            return e;
        },
        trim: b && !b.call("﻿ ") ? function(e) {
            return e == null ? "" : b.call(e);
        } : function(e) {
            return e == null ? "" : (e + "").replace(x, "");
        },
        makeArray: function(e, t) {
            var n = t || [];
            e != null && (H(Object(e)) ? w.merge(n, typeof e == "string" ? [ e ] : e) : d.call(n, e));
            return n;
        },
        inArray: function(e, t, n) {
            var r;
            if (t) {
                if (m) return m.call(t, e, n);
                r = t.length;
                n = n ? n < 0 ? Math.max(0, r + n) : n : 0;
                for (; n < r; n++) if (n in t && t[n] === e) return n;
            }
            return -1;
        },
        merge: function(e, n) {
            var r = n.length, i = e.length, s = 0;
            if (typeof r == "number") for (; s < r; s++) e[i++] = n[s]; else while (n[s] !== t) e[i++] = n[s++];
            e.length = i;
            return e;
        },
        grep: function(e, t, n) {
            var r, i = [], s = 0, o = e.length;
            n = !!n;
            for (; s < o; s++) {
                r = !!t(e[s], s);
                n !== r && i.push(e[s]);
            }
            return i;
        },
        map: function(e, t, n) {
            var r, i = 0, s = e.length, o = H(e), u = [];
            if (o) for (; i < s; i++) {
                r = t(e[i], i, n);
                r != null && (u[u.length] = r);
            } else for (i in e) {
                r = t(e[i], i, n);
                r != null && (u[u.length] = r);
            }
            return p.apply([], u);
        },
        guid: 1,
        proxy: function(e, n) {
            var r, i, s;
            if (typeof n == "string") {
                s = e[n];
                n = e;
                e = s;
            }
            if (!w.isFunction(e)) return t;
            r = v.call(arguments, 2);
            i = function() {
                return e.apply(n || this, r.concat(v.call(arguments)));
            };
            i.guid = e.guid = e.guid || w.guid++;
            return i;
        },
        access: function(e, n, r, i, s, o, u) {
            var a = 0, f = e.length, l = r == null;
            if (w.type(r) === "object") {
                s = !0;
                for (a in r) w.access(e, n, a, r[a], !0, o, u);
            } else if (i !== t) {
                s = !0;
                w.isFunction(i) || (u = !0);
                if (l) if (u) {
                    n.call(e, i);
                    n = null;
                } else {
                    l = n;
                    n = function(e, t, n) {
                        return l.call(w(e), n);
                    };
                }
                if (n) for (; a < f; a++) n(e[a], r, u ? i : i.call(e[a], a, n(e[a], r)));
            }
            return s ? e : l ? n.call(e) : f ? n(e[0], r) : o;
        },
        now: function() {
            return (new Date).getTime();
        },
        swap: function(e, t, n, r) {
            var i, s, o = {};
            for (s in t) {
                o[s] = e.style[s];
                e.style[s] = t[s];
            }
            i = n.apply(e, r || []);
            for (s in t) e.style[s] = o[s];
            return i;
        }
    });
    w.ready.promise = function(t) {
        if (!n) {
            n = w.Deferred();
            if (o.readyState === "complete") setTimeout(w.ready); else if (o.addEventListener) {
                o.addEventListener("DOMContentLoaded", D, !1);
                e.addEventListener("load", D, !1);
            } else {
                o.attachEvent("onreadystatechange", D);
                e.attachEvent("onload", D);
                var r = !1;
                try {
                    r = e.frameElement == null && o.documentElement;
                } catch (i) {}
                r && r.doScroll && function s() {
                    if (!w.isReady) {
                        try {
                            r.doScroll("left");
                        } catch (e) {
                            return setTimeout(s, 50);
                        }
                        P();
                        w.ready();
                    }
                }();
            }
        }
        return n.promise(t);
    };
    w.each("Boolean Number String Function Array Date RegExp Object Error".split(" "), function(e, t) {
        l["[object " + t + "]"] = t.toLowerCase();
    });
    r = w(o);
    (function(e, t) {
        function ot(e, t, n, i) {
            var s, o, u, a, f, l, p, m, g, w;
            (t ? t.ownerDocument || t : E) !== h && c(t);
            t = t || h;
            n = n || [];
            if (!e || typeof e != "string") return n;
            if ((a = t.nodeType) !== 1 && a !== 9) return [];
            if (d && !i) {
                if (s = Z.exec(e)) if (u = s[1]) {
                    if (a === 9) {
                        o = t.getElementById(u);
                        if (!o || !o.parentNode) return n;
                        if (o.id === u) {
                            n.push(o);
                            return n;
                        }
                    } else if (t.ownerDocument && (o = t.ownerDocument.getElementById(u)) && y(t, o) && o.id === u) {
                        n.push(o);
                        return n;
                    }
                } else {
                    if (s[2]) {
                        H.apply(n, t.getElementsByTagName(e));
                        return n;
                    }
                    if ((u = s[3]) && r.getElementsByClassName && t.getElementsByClassName) {
                        H.apply(n, t.getElementsByClassName(u));
                        return n;
                    }
                }
                if (r.qsa && (!v || !v.test(e))) {
                    m = p = b;
                    g = t;
                    w = a === 9 && e;
                    if (a === 1 && t.nodeName.toLowerCase() !== "object") {
                        l = bt(e);
                        (p = t.getAttribute("id")) ? m = p.replace(nt, "\\$&") : t.setAttribute("id", m);
                        m = "[id='" + m + "'] ";
                        f = l.length;
                        while (f--) l[f] = m + wt(l[f]);
                        g = $.test(e) && t.parentNode || t;
                        w = l.join(",");
                    }
                    if (w) try {
                        H.apply(n, g.querySelectorAll(w));
                        return n;
                    } catch (S) {} finally {
                        p || t.removeAttribute("id");
                    }
                }
            }
            return Lt(e.replace(W, "$1"), t, n, i);
        }
        function ut(e) {
            return Y.test(e + "");
        }
        function at() {
            function t(n, r) {
                e.push(n += " ") > s.cacheLength && delete t[e.shift()];
                return t[n] = r;
            }
            var e = [];
            return t;
        }
        function ft(e) {
            e[b] = !0;
            return e;
        }
        function lt(e) {
            var t = h.createElement("div");
            try {
                return !!e(t);
            } catch (n) {
                return !1;
            } finally {
                t.parentNode && t.parentNode.removeChild(t);
                t = null;
            }
        }
        function ct(e, t, n) {
            e = e.split("|");
            var r, i = e.length, o = n ? null : t;
            while (i--) if (!(r = s.attrHandle[e[i]]) || r === t) s.attrHandle[e[i]] = o;
        }
        function ht(e, t) {
            var n = e.getAttributeNode(t);
            return n && n.specified ? n.value : e[t] === !0 ? t.toLowerCase() : null;
        }
        function pt(e, t) {
            return e.getAttribute(t, t.toLowerCase() === "type" ? 1 : 2);
        }
        function dt(e) {
            if (e.nodeName.toLowerCase() === "input") return e.defaultValue;
        }
        function vt(e, t) {
            var n = t && e, r = n && e.nodeType === 1 && t.nodeType === 1 && (~t.sourceIndex || O) - (~e.sourceIndex || O);
            if (r) return r;
            if (n) while (n = n.nextSibling) if (n === t) return -1;
            return e ? 1 : -1;
        }
        function mt(e) {
            return function(t) {
                var n = t.nodeName.toLowerCase();
                return n === "input" && t.type === e;
            };
        }
        function gt(e) {
            return function(t) {
                var n = t.nodeName.toLowerCase();
                return (n === "input" || n === "button") && t.type === e;
            };
        }
        function yt(e) {
            return ft(function(t) {
                t = +t;
                return ft(function(n, r) {
                    var i, s = e([], n.length, t), o = s.length;
                    while (o--) n[i = s[o]] && (n[i] = !(r[i] = n[i]));
                });
            });
        }
        function bt(e, t) {
            var n, r, i, o, u, a, f, l = N[e + " "];
            if (l) return t ? 0 : l.slice(0);
            u = e;
            a = [];
            f = s.preFilter;
            while (u) {
                if (!n || (r = X.exec(u))) {
                    r && (u = u.slice(r[0].length) || u);
                    a.push(i = []);
                }
                n = !1;
                if (r = V.exec(u)) {
                    n = r.shift();
                    i.push({
                        value: n,
                        type: r[0].replace(W, " ")
                    });
                    u = u.slice(n.length);
                }
                for (o in s.filter) if ((r = G[o].exec(u)) && (!f[o] || (r = f[o](r)))) {
                    n = r.shift();
                    i.push({
                        value: n,
                        type: o,
                        matches: r
                    });
                    u = u.slice(n.length);
                }
                if (!n) break;
            }
            return t ? u.length : u ? ot.error(e) : N(e, a).slice(0);
        }
        function wt(e) {
            var t = 0, n = e.length, r = "";
            for (; t < n; t++) r += e[t].value;
            return r;
        }
        function Et(e, t, n) {
            var r = t.dir, s = n && r === "parentNode", o = x++;
            return t.first ? function(t, n, i) {
                while (t = t[r]) if (t.nodeType === 1 || s) return e(t, n, i);
            } : function(t, n, u) {
                var a, f, l, c = S + " " + o;
                if (u) {
                    while (t = t[r]) if (t.nodeType === 1 || s) if (e(t, n, u)) return !0;
                } else while (t = t[r]) if (t.nodeType === 1 || s) {
                    l = t[b] || (t[b] = {});
                    if ((f = l[r]) && f[0] === c) {
                        if ((a = f[1]) === !0 || a === i) return a === !0;
                    } else {
                        f = l[r] = [ c ];
                        f[1] = e(t, n, u) || i;
                        if (f[1] === !0) return !0;
                    }
                }
            };
        }
        function St(e) {
            return e.length > 1 ? function(t, n, r) {
                var i = e.length;
                while (i--) if (!e[i](t, n, r)) return !1;
                return !0;
            } : e[0];
        }
        function xt(e, t, n, r, i) {
            var s, o = [], u = 0, a = e.length, f = t != null;
            for (; u < a; u++) if (s = e[u]) if (!n || n(s, r, i)) {
                o.push(s);
                f && t.push(u);
            }
            return o;
        }
        function Tt(e, t, n, r, i, s) {
            r && !r[b] && (r = Tt(r));
            i && !i[b] && (i = Tt(i, s));
            return ft(function(s, o, u, a) {
                var f, l, c, h = [], p = [], d = o.length, v = s || kt(t || "*", u.nodeType ? [ u ] : u, []), m = e && (s || !t) ? xt(v, h, e, u, a) : v, g = n ? i || (s ? e : d || r) ? [] : o : m;
                n && n(m, g, u, a);
                if (r) {
                    f = xt(g, p);
                    r(f, [], u, a);
                    l = f.length;
                    while (l--) if (c = f[l]) g[p[l]] = !(m[p[l]] = c);
                }
                if (s) {
                    if (i || e) {
                        if (i) {
                            f = [];
                            l = g.length;
                            while (l--) (c = g[l]) && f.push(m[l] = c);
                            i(null, g = [], f, a);
                        }
                        l = g.length;
                        while (l--) (c = g[l]) && (f = i ? j.call(s, c) : h[l]) > -1 && (s[f] = !(o[f] = c));
                    }
                } else {
                    g = xt(g === o ? g.splice(d, g.length) : g);
                    i ? i(null, o, g, a) : H.apply(o, g);
                }
            });
        }
        function Nt(e) {
            var t, n, r, i = e.length, o = s.relative[e[0].type], u = o || s.relative[" "], a = o ? 1 : 0, l = Et(function(e) {
                return e === t;
            }, u, !0), c = Et(function(e) {
                return j.call(t, e) > -1;
            }, u, !0), h = [ function(e, n, r) {
                return !o && (r || n !== f) || ((t = n).nodeType ? l(e, n, r) : c(e, n, r));
            } ];
            for (; a < i; a++) if (n = s.relative[e[a].type]) h = [ Et(St(h), n) ]; else {
                n = s.filter[e[a].type].apply(null, e[a].matches);
                if (n[b]) {
                    r = ++a;
                    for (; r < i; r++) if (s.relative[e[r].type]) break;
                    return Tt(a > 1 && St(h), a > 1 && wt(e.slice(0, a - 1).concat({
                        value: e[a - 2].type === " " ? "*" : ""
                    })).replace(W, "$1"), n, a < r && Nt(e.slice(a, r)), r < i && Nt(e = e.slice(r)), r < i && wt(e));
                }
                h.push(n);
            }
            return St(h);
        }
        function Ct(e, t) {
            var n = 0, r = t.length > 0, o = e.length > 0, u = function(u, a, l, c, p) {
                var d, v, m, g = [], y = 0, b = "0", w = u && [], E = p != null, x = f, T = u || o && s.find.TAG("*", p && a.parentNode || a), N = S += x == null ? 1 : Math.random() || .1;
                if (E) {
                    f = a !== h && a;
                    i = n;
                }
                for (; (d = T[b]) != null; b++) {
                    if (o && d) {
                        v = 0;
                        while (m = e[v++]) if (m(d, a, l)) {
                            c.push(d);
                            break;
                        }
                        if (E) {
                            S = N;
                            i = ++n;
                        }
                    }
                    if (r) {
                        (d = !m && d) && y--;
                        u && w.push(d);
                    }
                }
                y += b;
                if (r && b !== y) {
                    v = 0;
                    while (m = t[v++]) m(w, g, a, l);
                    if (u) {
                        if (y > 0) while (b--) !w[b] && !g[b] && (g[b] = D.call(c));
                        g = xt(g);
                    }
                    H.apply(c, g);
                    E && !u && g.length > 0 && y + t.length > 1 && ot.uniqueSort(c);
                }
                if (E) {
                    S = N;
                    f = x;
                }
                return w;
            };
            return r ? ft(u) : u;
        }
        function kt(e, t, n) {
            var r = 0, i = t.length;
            for (; r < i; r++) ot(e, t[r], n);
            return n;
        }
        function Lt(e, t, n, i) {
            var o, u, f, l, c, h = bt(e);
            if (!i && h.length === 1) {
                u = h[0] = h[0].slice(0);
                if (u.length > 2 && (f = u[0]).type === "ID" && r.getById && t.nodeType === 9 && d && s.relative[u[1].type]) {
                    t = (s.find.ID(f.matches[0].replace(rt, it), t) || [])[0];
                    if (!t) return n;
                    e = e.slice(u.shift().value.length);
                }
                o = G.needsContext.test(e) ? 0 : u.length;
                while (o--) {
                    f = u[o];
                    if (s.relative[l = f.type]) break;
                    if (c = s.find[l]) if (i = c(f.matches[0].replace(rt, it), $.test(u[0].type) && t.parentNode || t)) {
                        u.splice(o, 1);
                        e = i.length && wt(u);
                        if (!e) {
                            H.apply(n, i);
                            return n;
                        }
                        break;
                    }
                }
            }
            a(e, h)(i, t, !d, n, $.test(e));
            return n;
        }
        function At() {}
        var n, r, i, s, o, u, a, f, l, c, h, p, d, v, m, g, y, b = "sizzle" + -(new Date), E = e.document, S = 0, x = 0, T = at(), N = at(), C = at(), k = !1, L = function() {
            return 0;
        }, A = typeof t, O = 1 << 31, M = {}.hasOwnProperty, _ = [], D = _.pop, P = _.push, H = _.push, B = _.slice, j = _.indexOf || function(e) {
            var t = 0, n = this.length;
            for (; t < n; t++) if (this[t] === e) return t;
            return -1;
        }, F = "checked|selected|async|autofocus|autoplay|controls|defer|disabled|hidden|ismap|loop|multiple|open|readonly|required|scoped", I = "[\\x20\\t\\r\\n\\f]", q = "(?:\\\\.|[\\w-]|[^\\x00-\\xa0])+", R = q.replace("w", "w#"), U = "\\[" + I + "*(" + q + ")" + I + "*(?:([*^$|!~]?=)" + I + "*(?:(['\"])((?:\\\\.|[^\\\\])*?)\\3|(" + R + ")|)|)" + I + "*\\]", z = ":(" + q + ")(?:\\(((['\"])((?:\\\\.|[^\\\\])*?)\\3|((?:\\\\.|[^\\\\()[\\]]|" + U.replace(3, 8) + ")*)|.*)\\)|)", W = new RegExp("^" + I + "+|((?:^|[^\\\\])(?:\\\\.)*)" + I + "+$", "g"), X = new RegExp("^" + I + "*," + I + "*"), V = new RegExp("^" + I + "*([>+~]|" + I + ")" + I + "*"), $ = new RegExp(I + "*[+~]"), J = new RegExp("=" + I + "*([^\\]'\"]*)" + I + "*\\]", "g"), K = new RegExp(z), Q = new RegExp("^" + R + "$"), G = {
            ID: new RegExp("^#(" + q + ")"),
            CLASS: new RegExp("^\\.(" + q + ")"),
            TAG: new RegExp("^(" + q.replace("w", "w*") + ")"),
            ATTR: new RegExp("^" + U),
            PSEUDO: new RegExp("^" + z),
            CHILD: new RegExp("^:(only|first|last|nth|nth-last)-(child|of-type)(?:\\(" + I + "*(even|odd|(([+-]|)(\\d*)n|)" + I + "*(?:([+-]|)" + I + "*(\\d+)|))" + I + "*\\)|)", "i"),
            bool: new RegExp("^(?:" + F + ")$", "i"),
            needsContext: new RegExp("^" + I + "*[>+~]|:(even|odd|eq|gt|lt|nth|first|last)(?:\\(" + I + "*((?:-\\d)?\\d*)" + I + "*\\)|)(?=[^-]|$)", "i")
        }, Y = /^[^{]+\{\s*\[native \w/, Z = /^(?:#([\w-]+)|(\w+)|\.([\w-]+))$/, et = /^(?:input|select|textarea|button)$/i, tt = /^h\d$/i, nt = /'|\\/g, rt = new RegExp("\\\\([\\da-f]{1,6}" + I + "?|(" + I + ")|.)", "ig"), it = function(e, t, n) {
            var r = "0x" + t - 65536;
            return r !== r || n ? t : r < 0 ? String.fromCharCode(r + 65536) : String.fromCharCode(r >> 10 | 55296, r & 1023 | 56320);
        };
        try {
            H.apply(_ = B.call(E.childNodes), E.childNodes);
            _[E.childNodes.length].nodeType;
        } catch (st) {
            H = {
                apply: _.length ? function(e, t) {
                    P.apply(e, B.call(t));
                } : function(e, t) {
                    var n = e.length, r = 0;
                    while (e[n++] = t[r++]) ;
                    e.length = n - 1;
                }
            };
        }
        u = ot.isXML = function(e) {
            var t = e && (e.ownerDocument || e).documentElement;
            return t ? t.nodeName !== "HTML" : !1;
        };
        r = ot.support = {};
        c = ot.setDocument = function(e) {
            var t = e ? e.ownerDocument || e : E, n = t.parentWindow;
            if (t === h || t.nodeType !== 9 || !t.documentElement) return h;
            h = t;
            p = t.documentElement;
            d = !u(t);
            n && n.frameElement && n.attachEvent("onbeforeunload", function() {
                c();
            });
            r.attributes = lt(function(e) {
                e.innerHTML = "<a href='#'></a>";
                ct("type|href|height|width", pt, e.firstChild.getAttribute("href") === "#");
                ct(F, ht, e.getAttribute("disabled") == null);
                e.className = "i";
                return !e.getAttribute("className");
            });
            r.input = lt(function(e) {
                e.innerHTML = "<input>";
                e.firstChild.setAttribute("value", "");
                return e.firstChild.getAttribute("value") === "";
            });
            ct("value", dt, r.attributes && r.input);
            r.getElementsByTagName = lt(function(e) {
                e.appendChild(t.createComment(""));
                return !e.getElementsByTagName("*").length;
            });
            r.getElementsByClassName = lt(function(e) {
                e.innerHTML = "<div class='a'></div><div class='a i'></div>";
                e.firstChild.className = "i";
                return e.getElementsByClassName("i").length === 2;
            });
            r.getById = lt(function(e) {
                p.appendChild(e).id = b;
                return !t.getElementsByName || !t.getElementsByName(b).length;
            });
            if (r.getById) {
                s.find.ID = function(e, t) {
                    if (typeof t.getElementById !== A && d) {
                        var n = t.getElementById(e);
                        return n && n.parentNode ? [ n ] : [];
                    }
                };
                s.filter.ID = function(e) {
                    var t = e.replace(rt, it);
                    return function(e) {
                        return e.getAttribute("id") === t;
                    };
                };
            } else {
                delete s.find.ID;
                s.filter.ID = function(e) {
                    var t = e.replace(rt, it);
                    return function(e) {
                        var n = typeof e.getAttributeNode !== A && e.getAttributeNode("id");
                        return n && n.value === t;
                    };
                };
            }
            s.find.TAG = r.getElementsByTagName ? function(e, t) {
                if (typeof t.getElementsByTagName !== A) return t.getElementsByTagName(e);
            } : function(e, t) {
                var n, r = [], i = 0, s = t.getElementsByTagName(e);
                if (e === "*") {
                    while (n = s[i++]) n.nodeType === 1 && r.push(n);
                    return r;
                }
                return s;
            };
            s.find.CLASS = r.getElementsByClassName && function(e, t) {
                if (typeof t.getElementsByClassName !== A && d) return t.getElementsByClassName(e);
            };
            m = [];
            v = [];
            if (r.qsa = ut(t.querySelectorAll)) {
                lt(function(e) {
                    e.innerHTML = "<select><option selected=''></option></select>";
                    e.querySelectorAll("[selected]").length || v.push("\\[" + I + "*(?:value|" + F + ")");
                    e.querySelectorAll(":checked").length || v.push(":checked");
                });
                lt(function(e) {
                    var n = t.createElement("input");
                    n.setAttribute("type", "hidden");
                    e.appendChild(n).setAttribute("t", "");
                    e.querySelectorAll("[t^='']").length && v.push("[*^$]=" + I + "*(?:''|\"\")");
                    e.querySelectorAll(":enabled").length || v.push(":enabled", ":disabled");
                    e.querySelectorAll("*,:x");
                    v.push(",.*:");
                });
            }
            (r.matchesSelector = ut(g = p.webkitMatchesSelector || p.mozMatchesSelector || p.oMatchesSelector || p.msMatchesSelector)) && lt(function(e) {
                r.disconnectedMatch = g.call(e, "div");
                g.call(e, "[s!='']:x");
                m.push("!=", z);
            });
            v = v.length && new RegExp(v.join("|"));
            m = m.length && new RegExp(m.join("|"));
            y = ut(p.contains) || p.compareDocumentPosition ? function(e, t) {
                var n = e.nodeType === 9 ? e.documentElement : e, r = t && t.parentNode;
                return e === r || !!r && r.nodeType === 1 && !!(n.contains ? n.contains(r) : e.compareDocumentPosition && e.compareDocumentPosition(r) & 16);
            } : function(e, t) {
                if (t) while (t = t.parentNode) if (t === e) return !0;
                return !1;
            };
            r.sortDetached = lt(function(e) {
                return e.compareDocumentPosition(t.createElement("div")) & 1;
            });
            L = p.compareDocumentPosition ? function(e, n) {
                if (e === n) {
                    k = !0;
                    return 0;
                }
                var i = n.compareDocumentPosition && e.compareDocumentPosition && e.compareDocumentPosition(n);
                if (i) return i & 1 || !r.sortDetached && n.compareDocumentPosition(e) === i ? e === t || y(E, e) ? -1 : n === t || y(E, n) ? 1 : l ? j.call(l, e) - j.call(l, n) : 0 : i & 4 ? -1 : 1;
                return e.compareDocumentPosition ? -1 : 1;
            } : function(e, n) {
                var r, i = 0, s = e.parentNode, o = n.parentNode, u = [ e ], a = [ n ];
                if (e === n) {
                    k = !0;
                    return 0;
                }
                if (!s || !o) return e === t ? -1 : n === t ? 1 : s ? -1 : o ? 1 : l ? j.call(l, e) - j.call(l, n) : 0;
                if (s === o) return vt(e, n);
                r = e;
                while (r = r.parentNode) u.unshift(r);
                r = n;
                while (r = r.parentNode) a.unshift(r);
                while (u[i] === a[i]) i++;
                return i ? vt(u[i], a[i]) : u[i] === E ? -1 : a[i] === E ? 1 : 0;
            };
            return t;
        };
        ot.matches = function(e, t) {
            return ot(e, null, null, t);
        };
        ot.matchesSelector = function(e, t) {
            (e.ownerDocument || e) !== h && c(e);
            t = t.replace(J, "='$1']");
            if (r.matchesSelector && d && (!m || !m.test(t)) && (!v || !v.test(t))) try {
                var n = g.call(e, t);
                if (n || r.disconnectedMatch || e.document && e.document.nodeType !== 11) return n;
            } catch (i) {}
            return ot(t, h, null, [ e ]).length > 0;
        };
        ot.contains = function(e, t) {
            (e.ownerDocument || e) !== h && c(e);
            return y(e, t);
        };
        ot.attr = function(e, n) {
            (e.ownerDocument || e) !== h && c(e);
            var i = s.attrHandle[n.toLowerCase()], o = i && M.call(s.attrHandle, n.toLowerCase()) ? i(e, n, !d) : t;
            return o === t ? r.attributes || !d ? e.getAttribute(n) : (o = e.getAttributeNode(n)) && o.specified ? o.value : null : o;
        };
        ot.error = function(e) {
            throw new Error("Syntax error, unrecognized expression: " + e);
        };
        ot.uniqueSort = function(e) {
            var t, n = [], i = 0, s = 0;
            k = !r.detectDuplicates;
            l = !r.sortStable && e.slice(0);
            e.sort(L);
            if (k) {
                while (t = e[s++]) t === e[s] && (i = n.push(s));
                while (i--) e.splice(n[i], 1);
            }
            return e;
        };
        o = ot.getText = function(e) {
            var t, n = "", r = 0, i = e.nodeType;
            if (!i) for (; t = e[r]; r++) n += o(t); else if (i === 1 || i === 9 || i === 11) {
                if (typeof e.textContent == "string") return e.textContent;
                for (e = e.firstChild; e; e = e.nextSibling) n += o(e);
            } else if (i === 3 || i === 4) return e.nodeValue;
            return n;
        };
        s = ot.selectors = {
            cacheLength: 50,
            createPseudo: ft,
            match: G,
            attrHandle: {},
            find: {},
            relative: {
                ">": {
                    dir: "parentNode",
                    first: !0
                },
                " ": {
                    dir: "parentNode"
                },
                "+": {
                    dir: "previousSibling",
                    first: !0
                },
                "~": {
                    dir: "previousSibling"
                }
            },
            preFilter: {
                ATTR: function(e) {
                    e[1] = e[1].replace(rt, it);
                    e[3] = (e[4] || e[5] || "").replace(rt, it);
                    e[2] === "~=" && (e[3] = " " + e[3] + " ");
                    return e.slice(0, 4);
                },
                CHILD: function(e) {
                    e[1] = e[1].toLowerCase();
                    if (e[1].slice(0, 3) === "nth") {
                        e[3] || ot.error(e[0]);
                        e[4] = +(e[4] ? e[5] + (e[6] || 1) : 2 * (e[3] === "even" || e[3] === "odd"));
                        e[5] = +(e[7] + e[8] || e[3] === "odd");
                    } else e[3] && ot.error(e[0]);
                    return e;
                },
                PSEUDO: function(e) {
                    var n, r = !e[5] && e[2];
                    if (G.CHILD.test(e[0])) return null;
                    if (e[3] && e[4] !== t) e[2] = e[4]; else if (r && K.test(r) && (n = bt(r, !0)) && (n = r.indexOf(")", r.length - n) - r.length)) {
                        e[0] = e[0].slice(0, n);
                        e[2] = r.slice(0, n);
                    }
                    return e.slice(0, 3);
                }
            },
            filter: {
                TAG: function(e) {
                    var t = e.replace(rt, it).toLowerCase();
                    return e === "*" ? function() {
                        return !0;
                    } : function(e) {
                        return e.nodeName && e.nodeName.toLowerCase() === t;
                    };
                },
                CLASS: function(e) {
                    var t = T[e + " "];
                    return t || (t = new RegExp("(^|" + I + ")" + e + "(" + I + "|$)")) && T(e, function(e) {
                        return t.test(typeof e.className == "string" && e.className || typeof e.getAttribute !== A && e.getAttribute("class") || "");
                    });
                },
                ATTR: function(e, t, n) {
                    return function(r) {
                        var i = ot.attr(r, e);
                        if (i == null) return t === "!=";
                        if (!t) return !0;
                        i += "";
                        return t === "=" ? i === n : t === "!=" ? i !== n : t === "^=" ? n && i.indexOf(n) === 0 : t === "*=" ? n && i.indexOf(n) > -1 : t === "$=" ? n && i.slice(-n.length) === n : t === "~=" ? (" " + i + " ").indexOf(n) > -1 : t === "|=" ? i === n || i.slice(0, n.length + 1) === n + "-" : !1;
                    };
                },
                CHILD: function(e, t, n, r, i) {
                    var s = e.slice(0, 3) !== "nth", o = e.slice(-4) !== "last", u = t === "of-type";
                    return r === 1 && i === 0 ? function(e) {
                        return !!e.parentNode;
                    } : function(t, n, a) {
                        var f, l, c, h, p, d, v = s !== o ? "nextSibling" : "previousSibling", m = t.parentNode, g = u && t.nodeName.toLowerCase(), y = !a && !u;
                        if (m) {
                            if (s) {
                                while (v) {
                                    c = t;
                                    while (c = c[v]) if (u ? c.nodeName.toLowerCase() === g : c.nodeType === 1) return !1;
                                    d = v = e === "only" && !d && "nextSibling";
                                }
                                return !0;
                            }
                            d = [ o ? m.firstChild : m.lastChild ];
                            if (o && y) {
                                l = m[b] || (m[b] = {});
                                f = l[e] || [];
                                p = f[0] === S && f[1];
                                h = f[0] === S && f[2];
                                c = p && m.childNodes[p];
                                while (c = ++p && c && c[v] || (h = p = 0) || d.pop()) if (c.nodeType === 1 && ++h && c === t) {
                                    l[e] = [ S, p, h ];
                                    break;
                                }
                            } else if (y && (f = (t[b] || (t[b] = {}))[e]) && f[0] === S) h = f[1]; else while (c = ++p && c && c[v] || (h = p = 0) || d.pop()) if ((u ? c.nodeName.toLowerCase() === g : c.nodeType === 1) && ++h) {
                                y && ((c[b] || (c[b] = {}))[e] = [ S, h ]);
                                if (c === t) break;
                            }
                            h -= i;
                            return h === r || h % r === 0 && h / r >= 0;
                        }
                    };
                },
                PSEUDO: function(e, t) {
                    var n, r = s.pseudos[e] || s.setFilters[e.toLowerCase()] || ot.error("unsupported pseudo: " + e);
                    if (r[b]) return r(t);
                    if (r.length > 1) {
                        n = [ e, e, "", t ];
                        return s.setFilters.hasOwnProperty(e.toLowerCase()) ? ft(function(e, n) {
                            var i, s = r(e, t), o = s.length;
                            while (o--) {
                                i = j.call(e, s[o]);
                                e[i] = !(n[i] = s[o]);
                            }
                        }) : function(e) {
                            return r(e, 0, n);
                        };
                    }
                    return r;
                }
            },
            pseudos: {
                not: ft(function(e) {
                    var t = [], n = [], r = a(e.replace(W, "$1"));
                    return r[b] ? ft(function(e, t, n, i) {
                        var s, o = r(e, null, i, []), u = e.length;
                        while (u--) if (s = o[u]) e[u] = !(t[u] = s);
                    }) : function(e, i, s) {
                        t[0] = e;
                        r(t, null, s, n);
                        return !n.pop();
                    };
                }),
                has: ft(function(e) {
                    return function(t) {
                        return ot(e, t).length > 0;
                    };
                }),
                contains: ft(function(e) {
                    return function(t) {
                        return (t.textContent || t.innerText || o(t)).indexOf(e) > -1;
                    };
                }),
                lang: ft(function(e) {
                    Q.test(e || "") || ot.error("unsupported lang: " + e);
                    e = e.replace(rt, it).toLowerCase();
                    return function(t) {
                        var n;
                        do if (n = d ? t.lang : t.getAttribute("xml:lang") || t.getAttribute("lang")) {
                            n = n.toLowerCase();
                            return n === e || n.indexOf(e + "-") === 0;
                        } while ((t = t.parentNode) && t.nodeType === 1);
                        return !1;
                    };
                }),
                target: function(t) {
                    var n = e.location && e.location.hash;
                    return n && n.slice(1) === t.id;
                },
                root: function(e) {
                    return e === p;
                },
                focus: function(e) {
                    return e === h.activeElement && (!h.hasFocus || h.hasFocus()) && !!(e.type || e.href || ~e.tabIndex);
                },
                enabled: function(e) {
                    return e.disabled === !1;
                },
                disabled: function(e) {
                    return e.disabled === !0;
                },
                checked: function(e) {
                    var t = e.nodeName.toLowerCase();
                    return t === "input" && !!e.checked || t === "option" && !!e.selected;
                },
                selected: function(e) {
                    e.parentNode && e.parentNode.selectedIndex;
                    return e.selected === !0;
                },
                empty: function(e) {
                    for (e = e.firstChild; e; e = e.nextSibling) if (e.nodeName > "@" || e.nodeType === 3 || e.nodeType === 4) return !1;
                    return !0;
                },
                parent: function(e) {
                    return !s.pseudos.empty(e);
                },
                header: function(e) {
                    return tt.test(e.nodeName);
                },
                input: function(e) {
                    return et.test(e.nodeName);
                },
                button: function(e) {
                    var t = e.nodeName.toLowerCase();
                    return t === "input" && e.type === "button" || t === "button";
                },
                text: function(e) {
                    var t;
                    return e.nodeName.toLowerCase() === "input" && e.type === "text" && ((t = e.getAttribute("type")) == null || t.toLowerCase() === e.type);
                },
                first: yt(function() {
                    return [ 0 ];
                }),
                last: yt(function(e, t) {
                    return [ t - 1 ];
                }),
                eq: yt(function(e, t, n) {
                    return [ n < 0 ? n + t : n ];
                }),
                even: yt(function(e, t) {
                    var n = 0;
                    for (; n < t; n += 2) e.push(n);
                    return e;
                }),
                odd: yt(function(e, t) {
                    var n = 1;
                    for (; n < t; n += 2) e.push(n);
                    return e;
                }),
                lt: yt(function(e, t, n) {
                    var r = n < 0 ? n + t : n;
                    for (; --r >= 0; ) e.push(r);
                    return e;
                }),
                gt: yt(function(e, t, n) {
                    var r = n < 0 ? n + t : n;
                    for (; ++r < t; ) e.push(r);
                    return e;
                })
            }
        };
        for (n in {
            radio: !0,
            checkbox: !0,
            file: !0,
            password: !0,
            image: !0
        }) s.pseudos[n] = mt(n);
        for (n in {
            submit: !0,
            reset: !0
        }) s.pseudos[n] = gt(n);
        a = ot.compile = function(e, t) {
            var n, r = [], i = [], s = C[e + " "];
            if (!s) {
                t || (t = bt(e));
                n = t.length;
                while (n--) {
                    s = Nt(t[n]);
                    s[b] ? r.push(s) : i.push(s);
                }
                s = C(e, Ct(i, r));
            }
            return s;
        };
        s.pseudos.nth = s.pseudos.eq;
        At.prototype = s.filters = s.pseudos;
        s.setFilters = new At;
        r.sortStable = b.split("").sort(L).join("") === b;
        c();
        [ 0, 0 ].sort(L);
        r.detectDuplicates = k;
        w.find = ot;
        w.expr = ot.selectors;
        w.expr[":"] = w.expr.pseudos;
        w.unique = ot.uniqueSort;
        w.text = ot.getText;
        w.isXMLDoc = ot.isXML;
        w.contains = ot.contains;
    })(e);
    var B = {};
    w.Callbacks = function(e) {
        e = typeof e == "string" ? B[e] || j(e) : w.extend({}, e);
        var n, r, i, s, o, u, a = [], f = !e.once && [], l = function(t) {
            r = e.memory && t;
            i = !0;
            o = u || 0;
            u = 0;
            s = a.length;
            n = !0;
            for (; a && o < s; o++) if (a[o].apply(t[0], t[1]) === !1 && e.stopOnFalse) {
                r = !1;
                break;
            }
            n = !1;
            a && (f ? f.length && l(f.shift()) : r ? a = [] : c.disable());
        }, c = {
            add: function() {
                if (a) {
                    var t = a.length;
                    (function i(t) {
                        w.each(t, function(t, n) {
                            var r = w.type(n);
                            r === "function" ? (!e.unique || !c.has(n)) && a.push(n) : n && n.length && r !== "string" && i(n);
                        });
                    })(arguments);
                    if (n) s = a.length; else if (r) {
                        u = t;
                        l(r);
                    }
                }
                return this;
            },
            remove: function() {
                a && w.each(arguments, function(e, t) {
                    var r;
                    while ((r = w.inArray(t, a, r)) > -1) {
                        a.splice(r, 1);
                        if (n) {
                            r <= s && s--;
                            r <= o && o--;
                        }
                    }
                });
                return this;
            },
            has: function(e) {
                return e ? w.inArray(e, a) > -1 : !!a && !!a.length;
            },
            empty: function() {
                a = [];
                s = 0;
                return this;
            },
            disable: function() {
                a = f = r = t;
                return this;
            },
            disabled: function() {
                return !a;
            },
            lock: function() {
                f = t;
                r || c.disable();
                return this;
            },
            locked: function() {
                return !f;
            },
            fireWith: function(e, t) {
                t = t || [];
                t = [ e, t.slice ? t.slice() : t ];
                a && (!i || f) && (n ? f.push(t) : l(t));
                return this;
            },
            fire: function() {
                c.fireWith(this, arguments);
                return this;
            },
            fired: function() {
                return !!i;
            }
        };
        return c;
    };
    w.extend({
        Deferred: function(e) {
            var t = [ [ "resolve", "done", w.Callbacks("once memory"), "resolved" ], [ "reject", "fail", w.Callbacks("once memory"), "rejected" ], [ "notify", "progress", w.Callbacks("memory") ] ], n = "pending", r = {
                state: function() {
                    return n;
                },
                always: function() {
                    i.done(arguments).fail(arguments);
                    return this;
                },
                then: function() {
                    var e = arguments;
                    return w.Deferred(function(n) {
                        w.each(t, function(t, s) {
                            var o = s[0], u = w.isFunction(e[t]) && e[t];
                            i[s[1]](function() {
                                var e = u && u.apply(this, arguments);
                                e && w.isFunction(e.promise) ? e.promise().done(n.resolve).fail(n.reject).progress(n.notify) : n[o + "With"](this === r ? n.promise() : this, u ? [ e ] : arguments);
                            });
                        });
                        e = null;
                    }).promise();
                },
                promise: function(e) {
                    return e != null ? w.extend(e, r) : r;
                }
            }, i = {};
            r.pipe = r.then;
            w.each(t, function(e, s) {
                var o = s[2], u = s[3];
                r[s[1]] = o.add;
                u && o.add(function() {
                    n = u;
                }, t[e ^ 1][2].disable, t[2][2].lock);
                i[s[0]] = function() {
                    i[s[0] + "With"](this === i ? r : this, arguments);
                    return this;
                };
                i[s[0] + "With"] = o.fireWith;
            });
            r.promise(i);
            e && e.call(i, i);
            return i;
        },
        when: function(e) {
            var t = 0, n = v.call(arguments), r = n.length, i = r !== 1 || e && w.isFunction(e.promise) ? r : 0, s = i === 1 ? e : w.Deferred(), o = function(e, t, n) {
                return function(r) {
                    t[e] = this;
                    n[e] = arguments.length > 1 ? v.call(arguments) : r;
                    n === u ? s.notifyWith(t, n) : --i || s.resolveWith(t, n);
                };
            }, u, a, f;
            if (r > 1) {
                u = new Array(r);
                a = new Array(r);
                f = new Array(r);
                for (; t < r; t++) n[t] && w.isFunction(n[t].promise) ? n[t].promise().done(o(t, f, n)).fail(s.reject).progress(o(t, a, u)) : --i;
            }
            i || s.resolveWith(f, n);
            return s.promise();
        }
    });
    w.support = function(t) {
        var n, r, s, u, a, f, l, c, h, p = o.createElement("div");
        p.setAttribute("className", "t");
        p.innerHTML = "  <link/><table></table><a href='/a'>a</a><input type='checkbox'/>";
        n = p.getElementsByTagName("*") || [];
        r = p.getElementsByTagName("a")[0];
        if (!r || !r.style || !n.length) return t;
        u = o.createElement("select");
        f = u.appendChild(o.createElement("option"));
        s = p.getElementsByTagName("input")[0];
        r.style.cssText = "top:1px;float:left;opacity:.5";
        t.getSetAttribute = p.className !== "t";
        t.leadingWhitespace = p.firstChild.nodeType === 3;
        t.tbody = !p.getElementsByTagName("tbody").length;
        t.htmlSerialize = !!p.getElementsByTagName("link").length;
        t.style = /top/.test(r.getAttribute("style"));
        t.hrefNormalized = r.getAttribute("href") === "/a";
        t.opacity = /^0.5/.test(r.style.opacity);
        t.cssFloat = !!r.style.cssFloat;
        t.checkOn = !!s.value;
        t.optSelected = f.selected;
        t.enctype = !!o.createElement("form").enctype;
        t.html5Clone = o.createElement("nav").cloneNode(!0).outerHTML !== "<:nav></:nav>";
        t.inlineBlockNeedsLayout = !1;
        t.shrinkWrapBlocks = !1;
        t.pixelPosition = !1;
        t.deleteExpando = !0;
        t.noCloneEvent = !0;
        t.reliableMarginRight = !0;
        t.boxSizingReliable = !0;
        s.checked = !0;
        t.noCloneChecked = s.cloneNode(!0).checked;
        u.disabled = !0;
        t.optDisabled = !f.disabled;
        try {
            delete p.test;
        } catch (d) {
            t.deleteExpando = !1;
        }
        s = o.createElement("input");
        s.setAttribute("value", "");
        t.input = s.getAttribute("value") === "";
        s.value = "t";
        s.setAttribute("type", "radio");
        t.radioValue = s.value === "t";
        s.setAttribute("checked", "t");
        s.setAttribute("name", "t");
        a = o.createDocumentFragment();
        a.appendChild(s);
        t.appendChecked = s.checked;
        t.checkClone = a.cloneNode(!0).cloneNode(!0).lastChild.checked;
        if (p.attachEvent) {
            p.attachEvent("onclick", function() {
                t.noCloneEvent = !1;
            });
            p.cloneNode(!0).click();
        }
        for (h in {
            submit: !0,
            change: !0,
            focusin: !0
        }) {
            p.setAttribute(l = "on" + h, "t");
            t[h + "Bubbles"] = l in e || p.attributes[l].expando === !1;
        }
        p.style.backgroundClip = "content-box";
        p.cloneNode(!0).style.backgroundClip = "";
        t.clearCloneStyle = p.style.backgroundClip === "content-box";
        for (h in w(t)) break;
        t.ownLast = h !== "0";
        w(function() {
            var n, r, s, u = "padding:0;margin:0;border:0;display:block;box-sizing:content-box;-moz-box-sizing:content-box;-webkit-box-sizing:content-box;", a = o.getElementsByTagName("body")[0];
            if (!a) return;
            n = o.createElement("div");
            n.style.cssText = "border:0;width:0;height:0;position:absolute;top:0;left:-9999px;margin-top:1px";
            a.appendChild(n).appendChild(p);
            p.innerHTML = "<table><tr><td></td><td>t</td></tr></table>";
            s = p.getElementsByTagName("td");
            s[0].style.cssText = "padding:0;margin:0;border:0;display:none";
            c = s[0].offsetHeight === 0;
            s[0].style.display = "";
            s[1].style.display = "none";
            t.reliableHiddenOffsets = c && s[0].offsetHeight === 0;
            p.innerHTML = "";
            p.style.cssText = "box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;padding:1px;border:1px;display:block;width:4px;margin-top:1%;position:absolute;top:1%;";
            w.swap(a, a.style.zoom != null ? {
                zoom: 1
            } : {}, function() {
                t.boxSizing = p.offsetWidth === 4;
            });
            if (e.getComputedStyle) {
                t.pixelPosition = (e.getComputedStyle(p, null) || {}).top !== "1%";
                t.boxSizingReliable = (e.getComputedStyle(p, null) || {
                    width: "4px"
                }).width === "4px";
                r = p.appendChild(o.createElement("div"));
                r.style.cssText = p.style.cssText = u;
                r.style.marginRight = r.style.width = "0";
                p.style.width = "1px";
                t.reliableMarginRight = !parseFloat((e.getComputedStyle(r, null) || {}).marginRight);
            }
            if (typeof p.style.zoom !== i) {
                p.innerHTML = "";
                p.style.cssText = u + "width:1px;padding:1px;display:inline;zoom:1";
                t.inlineBlockNeedsLayout = p.offsetWidth === 3;
                p.style.display = "block";
                p.innerHTML = "<div></div>";
                p.firstChild.style.width = "5px";
                t.shrinkWrapBlocks = p.offsetWidth !== 3;
                t.inlineBlockNeedsLayout && (a.style.zoom = 1);
            }
            a.removeChild(n);
            n = p = s = r = null;
        });
        n = u = a = f = r = s = null;
        return t;
    }({});
    var F = /(?:\{[\s\S]*\}|\[[\s\S]*\])$/, I = /([A-Z])/g;
    w.extend({
        cache: {},
        noData: {
            applet: !0,
            embed: !0,
            object: "clsid:D27CDB6E-AE6D-11cf-96B8-444553540000"
        },
        hasData: function(e) {
            e = e.nodeType ? w.cache[e[w.expando]] : e[w.expando];
            return !!e && !z(e);
        },
        data: function(e, t, n) {
            return q(e, t, n);
        },
        removeData: function(e, t) {
            return R(e, t);
        },
        _data: function(e, t, n) {
            return q(e, t, n, !0);
        },
        _removeData: function(e, t) {
            return R(e, t, !0);
        },
        acceptData: function(e) {
            if (e.nodeType && e.nodeType !== 1 && e.nodeType !== 9) return !1;
            var t = e.nodeName && w.noData[e.nodeName.toLowerCase()];
            return !t || t !== !0 && e.getAttribute("classid") === t;
        }
    });
    w.fn.extend({
        data: function(e, n) {
            var r, i, s = null, o = 0, u = this[0];
            if (e === t) {
                if (this.length) {
                    s = w.data(u);
                    if (u.nodeType === 1 && !w._data(u, "parsedAttrs")) {
                        r = u.attributes;
                        for (; o < r.length; o++) {
                            i = r[o].name;
                            if (i.indexOf("data-") === 0) {
                                i = w.camelCase(i.slice(5));
                                U(u, i, s[i]);
                            }
                        }
                        w._data(u, "parsedAttrs", !0);
                    }
                }
                return s;
            }
            return typeof e == "object" ? this.each(function() {
                w.data(this, e);
            }) : arguments.length > 1 ? this.each(function() {
                w.data(this, e, n);
            }) : u ? U(u, e, w.data(u, e)) : null;
        },
        removeData: function(e) {
            return this.each(function() {
                w.removeData(this, e);
            });
        }
    });
    w.extend({
        queue: function(e, t, n) {
            var r;
            if (e) {
                t = (t || "fx") + "queue";
                r = w._data(e, t);
                n && (!r || w.isArray(n) ? r = w._data(e, t, w.makeArray(n)) : r.push(n));
                return r || [];
            }
        },
        dequeue: function(e, t) {
            t = t || "fx";
            var n = w.queue(e, t), r = n.length, i = n.shift(), s = w._queueHooks(e, t), o = function() {
                w.dequeue(e, t);
            };
            if (i === "inprogress") {
                i = n.shift();
                r--;
            }
            if (i) {
                t === "fx" && n.unshift("inprogress");
                delete s.stop;
                i.call(e, o, s);
            }
            !r && s && s.empty.fire();
        },
        _queueHooks: function(e, t) {
            var n = t + "queueHooks";
            return w._data(e, n) || w._data(e, n, {
                empty: w.Callbacks("once memory").add(function() {
                    w._removeData(e, t + "queue");
                    w._removeData(e, n);
                })
            });
        }
    });
    w.fn.extend({
        queue: function(e, n) {
            var r = 2;
            if (typeof e != "string") {
                n = e;
                e = "fx";
                r--;
            }
            return arguments.length < r ? w.queue(this[0], e) : n === t ? this : this.each(function() {
                var t = w.queue(this, e, n);
                w._queueHooks(this, e);
                e === "fx" && t[0] !== "inprogress" && w.dequeue(this, e);
            });
        },
        dequeue: function(e) {
            return this.each(function() {
                w.dequeue(this, e);
            });
        },
        delay: function(e, t) {
            e = w.fx ? w.fx.speeds[e] || e : e;
            t = t || "fx";
            return this.queue(t, function(t, n) {
                var r = setTimeout(t, e);
                n.stop = function() {
                    clearTimeout(r);
                };
            });
        },
        clearQueue: function(e) {
            return this.queue(e || "fx", []);
        },
        promise: function(e, n) {
            var r, i = 1, s = w.Deferred(), o = this, u = this.length, a = function() {
                --i || s.resolveWith(o, [ o ]);
            };
            if (typeof e != "string") {
                n = e;
                e = t;
            }
            e = e || "fx";
            while (u--) {
                r = w._data(o[u], e + "queueHooks");
                if (r && r.empty) {
                    i++;
                    r.empty.add(a);
                }
            }
            a();
            return s.promise(n);
        }
    });
    var W, X, V = /[\t\r\n\f]/g, $ = /\r/g, J = /^(?:input|select|textarea|button|object)$/i, K = /^(?:a|area)$/i, Q = /^(?:checked|selected)$/i, G = w.support.getSetAttribute, Y = w.support.input;
    w.fn.extend({
        attr: function(e, t) {
            return w.access(this, w.attr, e, t, arguments.length > 1);
        },
        removeAttr: function(e) {
            return this.each(function() {
                w.removeAttr(this, e);
            });
        },
        prop: function(e, t) {
            return w.access(this, w.prop, e, t, arguments.length > 1);
        },
        removeProp: function(e) {
            e = w.propFix[e] || e;
            return this.each(function() {
                try {
                    this[e] = t;
                    delete this[e];
                } catch (n) {}
            });
        },
        addClass: function(e) {
            var t, n, r, i, s, o = 0, u = this.length, a = typeof e == "string" && e;
            if (w.isFunction(e)) return this.each(function(t) {
                w(this).addClass(e.call(this, t, this.className));
            });
            if (a) {
                t = (e || "").match(S) || [];
                for (; o < u; o++) {
                    n = this[o];
                    r = n.nodeType === 1 && (n.className ? (" " + n.className + " ").replace(V, " ") : " ");
                    if (r) {
                        s = 0;
                        while (i = t[s++]) r.indexOf(" " + i + " ") < 0 && (r += i + " ");
                        n.className = w.trim(r);
                    }
                }
            }
            return this;
        },
        removeClass: function(e) {
            var t, n, r, i, s, o = 0, u = this.length, a = arguments.length === 0 || typeof e == "string" && e;
            if (w.isFunction(e)) return this.each(function(t) {
                w(this).removeClass(e.call(this, t, this.className));
            });
            if (a) {
                t = (e || "").match(S) || [];
                for (; o < u; o++) {
                    n = this[o];
                    r = n.nodeType === 1 && (n.className ? (" " + n.className + " ").replace(V, " ") : "");
                    if (r) {
                        s = 0;
                        while (i = t[s++]) while (r.indexOf(" " + i + " ") >= 0) r = r.replace(" " + i + " ", " ");
                        n.className = e ? w.trim(r) : "";
                    }
                }
            }
            return this;
        },
        toggleClass: function(e, t) {
            var n = typeof e, r = typeof t == "boolean";
            return w.isFunction(e) ? this.each(function(n) {
                w(this).toggleClass(e.call(this, n, this.className, t), t);
            }) : this.each(function() {
                if (n === "string") {
                    var s, o = 0, u = w(this), a = t, f = e.match(S) || [];
                    while (s = f[o++]) {
                        a = r ? a : !u.hasClass(s);
                        u[a ? "addClass" : "removeClass"](s);
                    }
                } else if (n === i || n === "boolean") {
                    this.className && w._data(this, "__className__", this.className);
                    this.className = this.className || e === !1 ? "" : w._data(this, "__className__") || "";
                }
            });
        },
        hasClass: function(e) {
            var t = " " + e + " ", n = 0, r = this.length;
            for (; n < r; n++) if (this[n].nodeType === 1 && (" " + this[n].className + " ").replace(V, " ").indexOf(t) >= 0) return !0;
            return !1;
        },
        val: function(e) {
            var n, r, i, s = this[0];
            if (!arguments.length) {
                if (s) {
                    r = w.valHooks[s.type] || w.valHooks[s.nodeName.toLowerCase()];
                    if (r && "get" in r && (n = r.get(s, "value")) !== t) return n;
                    n = s.value;
                    return typeof n == "string" ? n.replace($, "") : n == null ? "" : n;
                }
                return;
            }
            i = w.isFunction(e);
            return this.each(function(n) {
                var s;
                if (this.nodeType !== 1) return;
                i ? s = e.call(this, n, w(this).val()) : s = e;
                s == null ? s = "" : typeof s == "number" ? s += "" : w.isArray(s) && (s = w.map(s, function(e) {
                    return e == null ? "" : e + "";
                }));
                r = w.valHooks[this.type] || w.valHooks[this.nodeName.toLowerCase()];
                if (!r || !("set" in r) || r.set(this, s, "value") === t) this.value = s;
            });
        }
    });
    w.extend({
        valHooks: {
            option: {
                get: function(e) {
                    var t = w.find.attr(e, "value");
                    return t != null ? t : e.text;
                }
            },
            select: {
                get: function(e) {
                    var t, n, r = e.options, i = e.selectedIndex, s = e.type === "select-one" || i < 0, o = s ? null : [], u = s ? i + 1 : r.length, a = i < 0 ? u : s ? i : 0;
                    for (; a < u; a++) {
                        n = r[a];
                        if ((n.selected || a === i) && (w.support.optDisabled ? !n.disabled : n.getAttribute("disabled") === null) && (!n.parentNode.disabled || !w.nodeName(n.parentNode, "optgroup"))) {
                            t = w(n).val();
                            if (s) return t;
                            o.push(t);
                        }
                    }
                    return o;
                },
                set: function(e, t) {
                    var n, r, i = e.options, s = w.makeArray(t), o = i.length;
                    while (o--) {
                        r = i[o];
                        if (r.selected = w.inArray(w(r).val(), s) >= 0) n = !0;
                    }
                    n || (e.selectedIndex = -1);
                    return s;
                }
            }
        },
        attr: function(e, n, r) {
            var s, o, u = e.nodeType;
            if (!e || u === 3 || u === 8 || u === 2) return;
            if (typeof e.getAttribute === i) return w.prop(e, n, r);
            if (u !== 1 || !w.isXMLDoc(e)) {
                n = n.toLowerCase();
                s = w.attrHooks[n] || (w.expr.match.bool.test(n) ? X : W);
            }
            if (r === t) {
                if (s && "get" in s && (o = s.get(e, n)) !== null) return o;
                o = w.find.attr(e, n);
                return o == null ? t : o;
            }
            if (r !== null) {
                if (s && "set" in s && (o = s.set(e, r, n)) !== t) return o;
                e.setAttribute(n, r + "");
                return r;
            }
            w.removeAttr(e, n);
        },
        removeAttr: function(e, t) {
            var n, r, i = 0, s = t && t.match(S);
            if (s && e.nodeType === 1) while (n = s[i++]) {
                r = w.propFix[n] || n;
                w.expr.match.bool.test(n) ? Y && G || !Q.test(n) ? e[r] = !1 : e[w.camelCase("default-" + n)] = e[r] = !1 : w.attr(e, n, "");
                e.removeAttribute(G ? n : r);
            }
        },
        attrHooks: {
            type: {
                set: function(e, t) {
                    if (!w.support.radioValue && t === "radio" && w.nodeName(e, "input")) {
                        var n = e.value;
                        e.setAttribute("type", t);
                        n && (e.value = n);
                        return t;
                    }
                }
            }
        },
        propFix: {
            "for": "htmlFor",
            "class": "className"
        },
        prop: function(e, n, r) {
            var i, s, o, u = e.nodeType;
            if (!e || u === 3 || u === 8 || u === 2) return;
            o = u !== 1 || !w.isXMLDoc(e);
            if (o) {
                n = w.propFix[n] || n;
                s = w.propHooks[n];
            }
            return r !== t ? s && "set" in s && (i = s.set(e, r, n)) !== t ? i : e[n] = r : s && "get" in s && (i = s.get(e, n)) !== null ? i : e[n];
        },
        propHooks: {
            tabIndex: {
                get: function(e) {
                    var t = w.find.attr(e, "tabindex");
                    return t ? parseInt(t, 10) : J.test(e.nodeName) || K.test(e.nodeName) && e.href ? 0 : -1;
                }
            }
        }
    });
    X = {
        set: function(e, t, n) {
            t === !1 ? w.removeAttr(e, n) : Y && G || !Q.test(n) ? e.setAttribute(!G && w.propFix[n] || n, n) : e[w.camelCase("default-" + n)] = e[n] = !0;
            return n;
        }
    };
    w.each(w.expr.match.bool.source.match(/\w+/g), function(e, n) {
        var r = w.expr.attrHandle[n] || w.find.attr;
        w.expr.attrHandle[n] = Y && G || !Q.test(n) ? function(e, n, i) {
            var s = w.expr.attrHandle[n], o = i ? t : (w.expr.attrHandle[n] = t) != r(e, n, i) ? n.toLowerCase() : null;
            w.expr.attrHandle[n] = s;
            return o;
        } : function(e, n, r) {
            return r ? t : e[w.camelCase("default-" + n)] ? n.toLowerCase() : null;
        };
    });
    if (!Y || !G) w.attrHooks.value = {
        set: function(e, t, n) {
            if (!w.nodeName(e, "input")) return W && W.set(e, t, n);
            e.defaultValue = t;
        }
    };
    if (!G) {
        W = {
            set: function(e, n, r) {
                var i = e.getAttributeNode(r);
                i || e.setAttributeNode(i = e.ownerDocument.createAttribute(r));
                i.value = n += "";
                return r === "value" || n === e.getAttribute(r) ? n : t;
            }
        };
        w.expr.attrHandle.id = w.expr.attrHandle.name = w.expr.attrHandle.coords = function(e, n, r) {
            var i;
            return r ? t : (i = e.getAttributeNode(n)) && i.value !== "" ? i.value : null;
        };
        w.valHooks.button = {
            get: function(e, n) {
                var r = e.getAttributeNode(n);
                return r && r.specified ? r.value : t;
            },
            set: W.set
        };
        w.attrHooks.contenteditable = {
            set: function(e, t, n) {
                W.set(e, t === "" ? !1 : t, n);
            }
        };
        w.each([ "width", "height" ], function(e, t) {
            w.attrHooks[t] = {
                set: function(e, n) {
                    if (n === "") {
                        e.setAttribute(t, "auto");
                        return n;
                    }
                }
            };
        });
    }
    w.support.hrefNormalized || w.each([ "href", "src" ], function(e, t) {
        w.propHooks[t] = {
            get: function(e) {
                return e.getAttribute(t, 4);
            }
        };
    });
    w.support.style || (w.attrHooks.style = {
        get: function(e) {
            return e.style.cssText || t;
        },
        set: function(e, t) {
            return e.style.cssText = t + "";
        }
    });
    w.support.optSelected || (w.propHooks.selected = {
        get: function(e) {
            var t = e.parentNode;
            if (t) {
                t.selectedIndex;
                t.parentNode && t.parentNode.selectedIndex;
            }
            return null;
        }
    });
    w.each([ "tabIndex", "readOnly", "maxLength", "cellSpacing", "cellPadding", "rowSpan", "colSpan", "useMap", "frameBorder", "contentEditable" ], function() {
        w.propFix[this.toLowerCase()] = this;
    });
    w.support.enctype || (w.propFix.enctype = "encoding");
    w.each([ "radio", "checkbox" ], function() {
        w.valHooks[this] = {
            set: function(e, t) {
                if (w.isArray(t)) return e.checked = w.inArray(w(e).val(), t) >= 0;
            }
        };
        w.support.checkOn || (w.valHooks[this].get = function(e) {
            return e.getAttribute("value") === null ? "on" : e.value;
        });
    });
    var Z = /^(?:input|select|textarea)$/i, et = /^key/, tt = /^(?:mouse|contextmenu)|click/, nt = /^(?:focusinfocus|focusoutblur)$/, rt = /^([^.]*)(?:\.(.+)|)$/;
    w.event = {
        global: {},
        add: function(e, n, r, s, o) {
            var u, a, f, l, c, h, p, d, v, m, g, y = w._data(e);
            if (!y) return;
            if (r.handler) {
                l = r;
                r = l.handler;
                o = l.selector;
            }
            r.guid || (r.guid = w.guid++);
            (a = y.events) || (a = y.events = {});
            if (!(h = y.handle)) {
                h = y.handle = function(e) {
                    return typeof w === i || !!e && w.event.triggered === e.type ? t : w.event.dispatch.apply(h.elem, arguments);
                };
                h.elem = e;
            }
            n = (n || "").match(S) || [ "" ];
            f = n.length;
            while (f--) {
                u = rt.exec(n[f]) || [];
                v = g = u[1];
                m = (u[2] || "").split(".").sort();
                if (!v) continue;
                c = w.event.special[v] || {};
                v = (o ? c.delegateType : c.bindType) || v;
                c = w.event.special[v] || {};
                p = w.extend({
                    type: v,
                    origType: g,
                    data: s,
                    handler: r,
                    guid: r.guid,
                    selector: o,
                    needsContext: o && w.expr.match.needsContext.test(o),
                    namespace: m.join(".")
                }, l);
                if (!(d = a[v])) {
                    d = a[v] = [];
                    d.delegateCount = 0;
                    if (!c.setup || c.setup.call(e, s, m, h) === !1) e.addEventListener ? e.addEventListener(v, h, !1) : e.attachEvent && e.attachEvent("on" + v, h);
                }
                if (c.add) {
                    c.add.call(e, p);
                    p.handler.guid || (p.handler.guid = r.guid);
                }
                o ? d.splice(d.delegateCount++, 0, p) : d.push(p);
                w.event.global[v] = !0;
            }
            e = null;
        },
        remove: function(e, t, n, r, i) {
            var s, o, u, a, f, l, c, h, p, d, v, m = w.hasData(e) && w._data(e);
            if (!m || !(l = m.events)) return;
            t = (t || "").match(S) || [ "" ];
            f = t.length;
            while (f--) {
                u = rt.exec(t[f]) || [];
                p = v = u[1];
                d = (u[2] || "").split(".").sort();
                if (!p) {
                    for (p in l) w.event.remove(e, p + t[f], n, r, !0);
                    continue;
                }
                c = w.event.special[p] || {};
                p = (r ? c.delegateType : c.bindType) || p;
                h = l[p] || [];
                u = u[2] && new RegExp("(^|\\.)" + d.join("\\.(?:.*\\.|)") + "(\\.|$)");
                a = s = h.length;
                while (s--) {
                    o = h[s];
                    if ((i || v === o.origType) && (!n || n.guid === o.guid) && (!u || u.test(o.namespace)) && (!r || r === o.selector || r === "**" && o.selector)) {
                        h.splice(s, 1);
                        o.selector && h.delegateCount--;
                        c.remove && c.remove.call(e, o);
                    }
                }
                if (a && !h.length) {
                    (!c.teardown || c.teardown.call(e, d, m.handle) === !1) && w.removeEvent(e, p, m.handle);
                    delete l[p];
                }
            }
            if (w.isEmptyObject(l)) {
                delete m.handle;
                w._removeData(e, "events");
            }
        },
        trigger: function(n, r, i, s) {
            var u, a, f, l, c, h, p, d = [ i || o ], v = y.call(n, "type") ? n.type : n, m = y.call(n, "namespace") ? n.namespace.split(".") : [];
            f = h = i = i || o;
            if (i.nodeType === 3 || i.nodeType === 8) return;
            if (nt.test(v + w.event.triggered)) return;
            if (v.indexOf(".") >= 0) {
                m = v.split(".");
                v = m.shift();
                m.sort();
            }
            a = v.indexOf(":") < 0 && "on" + v;
            n = n[w.expando] ? n : new w.Event(v, typeof n == "object" && n);
            n.isTrigger = s ? 2 : 3;
            n.namespace = m.join(".");
            n.namespace_re = n.namespace ? new RegExp("(^|\\.)" + m.join("\\.(?:.*\\.|)") + "(\\.|$)") : null;
            n.result = t;
            n.target || (n.target = i);
            r = r == null ? [ n ] : w.makeArray(r, [ n ]);
            c = w.event.special[v] || {};
            if (!s && c.trigger && c.trigger.apply(i, r) === !1) return;
            if (!s && !c.noBubble && !w.isWindow(i)) {
                l = c.delegateType || v;
                nt.test(l + v) || (f = f.parentNode);
                for (; f; f = f.parentNode) {
                    d.push(f);
                    h = f;
                }
                h === (i.ownerDocument || o) && d.push(h.defaultView || h.parentWindow || e);
            }
            p = 0;
            while ((f = d[p++]) && !n.isPropagationStopped()) {
                n.type = p > 1 ? l : c.bindType || v;
                u = (w._data(f, "events") || {})[n.type] && w._data(f, "handle");
                u && u.apply(f, r);
                u = a && f[a];
                u && w.acceptData(f) && u.apply && u.apply(f, r) === !1 && n.preventDefault();
            }
            n.type = v;
            if (!s && !n.isDefaultPrevented() && (!c._default || c._default.apply(d.pop(), r) === !1) && w.acceptData(i) && a && i[v] && !w.isWindow(i)) {
                h = i[a];
                h && (i[a] = null);
                w.event.triggered = v;
                try {
                    i[v]();
                } catch (g) {}
                w.event.triggered = t;
                h && (i[a] = h);
            }
            return n.result;
        },
        dispatch: function(e) {
            e = w.event.fix(e);
            var n, r, i, s, o, u = [], a = v.call(arguments), f = (w._data(this, "events") || {})[e.type] || [], l = w.event.special[e.type] || {};
            a[0] = e;
            e.delegateTarget = this;
            if (l.preDispatch && l.preDispatch.call(this, e) === !1) return;
            u = w.event.handlers.call(this, e, f);
            n = 0;
            while ((s = u[n++]) && !e.isPropagationStopped()) {
                e.currentTarget = s.elem;
                o = 0;
                while ((i = s.handlers[o++]) && !e.isImmediatePropagationStopped()) if (!e.namespace_re || e.namespace_re.test(i.namespace)) {
                    e.handleObj = i;
                    e.data = i.data;
                    r = ((w.event.special[i.origType] || {}).handle || i.handler).apply(s.elem, a);
                    if (r !== t && (e.result = r) === !1) {
                        e.preventDefault();
                        e.stopPropagation();
                    }
                }
            }
            l.postDispatch && l.postDispatch.call(this, e);
            return e.result;
        },
        handlers: function(e, n) {
            var r, i, s, o, u = [], a = n.delegateCount, f = e.target;
            if (a && f.nodeType && (!e.button || e.type !== "click")) for (; f != this; f = f.parentNode || this) if (f.nodeType === 1 && (f.disabled !== !0 || e.type !== "click")) {
                s = [];
                for (o = 0; o < a; o++) {
                    i = n[o];
                    r = i.selector + " ";
                    s[r] === t && (s[r] = i.needsContext ? w(r, this).index(f) >= 0 : w.find(r, this, null, [ f ]).length);
                    s[r] && s.push(i);
                }
                s.length && u.push({
                    elem: f,
                    handlers: s
                });
            }
            a < n.length && u.push({
                elem: this,
                handlers: n.slice(a)
            });
            return u;
        },
        fix: function(e) {
            if (e[w.expando]) return e;
            var t, n, r, i = e.type, s = e, u = this.fixHooks[i];
            u || (this.fixHooks[i] = u = tt.test(i) ? this.mouseHooks : et.test(i) ? this.keyHooks : {});
            r = u.props ? this.props.concat(u.props) : this.props;
            e = new w.Event(s);
            t = r.length;
            while (t--) {
                n = r[t];
                e[n] = s[n];
            }
            e.target || (e.target = s.srcElement || o);
            e.target.nodeType === 3 && (e.target = e.target.parentNode);
            e.metaKey = !!e.metaKey;
            return u.filter ? u.filter(e, s) : e;
        },
        props: "altKey bubbles cancelable ctrlKey currentTarget eventPhase metaKey relatedTarget shiftKey target timeStamp view which".split(" "),
        fixHooks: {},
        keyHooks: {
            props: "char charCode key keyCode".split(" "),
            filter: function(e, t) {
                e.which == null && (e.which = t.charCode != null ? t.charCode : t.keyCode);
                return e;
            }
        },
        mouseHooks: {
            props: "button buttons clientX clientY fromElement offsetX offsetY pageX pageY screenX screenY toElement".split(" "),
            filter: function(e, n) {
                var r, i, s, u = n.button, a = n.fromElement;
                if (e.pageX == null && n.clientX != null) {
                    i = e.target.ownerDocument || o;
                    s = i.documentElement;
                    r = i.body;
                    e.pageX = n.clientX + (s && s.scrollLeft || r && r.scrollLeft || 0) - (s && s.clientLeft || r && r.clientLeft || 0);
                    e.pageY = n.clientY + (s && s.scrollTop || r && r.scrollTop || 0) - (s && s.clientTop || r && r.clientTop || 0);
                }
                !e.relatedTarget && a && (e.relatedTarget = a === e.target ? n.toElement : a);
                !e.which && u !== t && (e.which = u & 1 ? 1 : u & 2 ? 3 : u & 4 ? 2 : 0);
                return e;
            }
        },
        special: {
            load: {
                noBubble: !0
            },
            focus: {
                trigger: function() {
                    if (this !== ot() && this.focus) try {
                        this.focus();
                        return !1;
                    } catch (e) {}
                },
                delegateType: "focusin"
            },
            blur: {
                trigger: function() {
                    if (this === ot() && this.blur) {
                        this.blur();
                        return !1;
                    }
                },
                delegateType: "focusout"
            },
            click: {
                trigger: function() {
                    if (w.nodeName(this, "input") && this.type === "checkbox" && this.click) {
                        this.click();
                        return !1;
                    }
                },
                _default: function(e) {
                    return w.nodeName(e.target, "a");
                }
            },
            beforeunload: {
                postDispatch: function(e) {
                    e.result !== t && (e.originalEvent.returnValue = e.result);
                }
            }
        },
        simulate: function(e, t, n, r) {
            var i = w.extend(new w.Event, n, {
                type: e,
                isSimulated: !0,
                originalEvent: {}
            });
            r ? w.event.trigger(i, null, t) : w.event.dispatch.call(t, i);
            i.isDefaultPrevented() && n.preventDefault();
        }
    };
    w.removeEvent = o.removeEventListener ? function(e, t, n) {
        e.removeEventListener && e.removeEventListener(t, n, !1);
    } : function(e, t, n) {
        var r = "on" + t;
        if (e.detachEvent) {
            typeof e[r] === i && (e[r] = null);
            e.detachEvent(r, n);
        }
    };
    w.Event = function(e, t) {
        if (!(this instanceof w.Event)) return new w.Event(e, t);
        if (e && e.type) {
            this.originalEvent = e;
            this.type = e.type;
            this.isDefaultPrevented = e.defaultPrevented || e.returnValue === !1 || e.getPreventDefault && e.getPreventDefault() ? it : st;
        } else this.type = e;
        t && w.extend(this, t);
        this.timeStamp = e && e.timeStamp || w.now();
        this[w.expando] = !0;
    };
    w.Event.prototype = {
        isDefaultPrevented: st,
        isPropagationStopped: st,
        isImmediatePropagationStopped: st,
        preventDefault: function() {
            var e = this.originalEvent;
            this.isDefaultPrevented = it;
            if (!e) return;
            e.preventDefault ? e.preventDefault() : e.returnValue = !1;
        },
        stopPropagation: function() {
            var e = this.originalEvent;
            this.isPropagationStopped = it;
            if (!e) return;
            e.stopPropagation && e.stopPropagation();
            e.cancelBubble = !0;
        },
        stopImmediatePropagation: function() {
            this.isImmediatePropagationStopped = it;
            this.stopPropagation();
        }
    };
    w.each({
        mouseenter: "mouseover",
        mouseleave: "mouseout"
    }, function(e, t) {
        w.event.special[e] = {
            delegateType: t,
            bindType: t,
            handle: function(e) {
                var n, r = this, i = e.relatedTarget, s = e.handleObj;
                if (!i || i !== r && !w.contains(r, i)) {
                    e.type = s.origType;
                    n = s.handler.apply(this, arguments);
                    e.type = t;
                }
                return n;
            }
        };
    });
    w.support.submitBubbles || (w.event.special.submit = {
        setup: function() {
            if (w.nodeName(this, "form")) return !1;
            w.event.add(this, "click._submit keypress._submit", function(e) {
                var n = e.target, r = w.nodeName(n, "input") || w.nodeName(n, "button") ? n.form : t;
                if (r && !w._data(r, "submitBubbles")) {
                    w.event.add(r, "submit._submit", function(e) {
                        e._submit_bubble = !0;
                    });
                    w._data(r, "submitBubbles", !0);
                }
            });
        },
        postDispatch: function(e) {
            if (e._submit_bubble) {
                delete e._submit_bubble;
                this.parentNode && !e.isTrigger && w.event.simulate("submit", this.parentNode, e, !0);
            }
        },
        teardown: function() {
            if (w.nodeName(this, "form")) return !1;
            w.event.remove(this, "._submit");
        }
    });
    w.support.changeBubbles || (w.event.special.change = {
        setup: function() {
            if (Z.test(this.nodeName)) {
                if (this.type === "checkbox" || this.type === "radio") {
                    w.event.add(this, "propertychange._change", function(e) {
                        e.originalEvent.propertyName === "checked" && (this._just_changed = !0);
                    });
                    w.event.add(this, "click._change", function(e) {
                        this._just_changed && !e.isTrigger && (this._just_changed = !1);
                        w.event.simulate("change", this, e, !0);
                    });
                }
                return !1;
            }
            w.event.add(this, "beforeactivate._change", function(e) {
                var t = e.target;
                if (Z.test(t.nodeName) && !w._data(t, "changeBubbles")) {
                    w.event.add(t, "change._change", function(e) {
                        this.parentNode && !e.isSimulated && !e.isTrigger && w.event.simulate("change", this.parentNode, e, !0);
                    });
                    w._data(t, "changeBubbles", !0);
                }
            });
        },
        handle: function(e) {
            var t = e.target;
            if (this !== t || e.isSimulated || e.isTrigger || t.type !== "radio" && t.type !== "checkbox") return e.handleObj.handler.apply(this, arguments);
        },
        teardown: function() {
            w.event.remove(this, "._change");
            return !Z.test(this.nodeName);
        }
    });
    w.support.focusinBubbles || w.each({
        focus: "focusin",
        blur: "focusout"
    }, function(e, t) {
        var n = 0, r = function(e) {
            w.event.simulate(t, e.target, w.event.fix(e), !0);
        };
        w.event.special[t] = {
            setup: function() {
                n++ === 0 && o.addEventListener(e, r, !0);
            },
            teardown: function() {
                --n === 0 && o.removeEventListener(e, r, !0);
            }
        };
    });
    w.fn.extend({
        on: function(e, n, r, i, s) {
            var o, u;
            if (typeof e == "object") {
                if (typeof n != "string") {
                    r = r || n;
                    n = t;
                }
                for (o in e) this.on(o, n, r, e[o], s);
                return this;
            }
            if (r == null && i == null) {
                i = n;
                r = n = t;
            } else if (i == null) if (typeof n == "string") {
                i = r;
                r = t;
            } else {
                i = r;
                r = n;
                n = t;
            }
            if (i === !1) i = st; else if (!i) return this;
            if (s === 1) {
                u = i;
                i = function(e) {
                    w().off(e);
                    return u.apply(this, arguments);
                };
                i.guid = u.guid || (u.guid = w.guid++);
            }
            return this.each(function() {
                w.event.add(this, e, i, r, n);
            });
        },
        one: function(e, t, n, r) {
            return this.on(e, t, n, r, 1);
        },
        off: function(e, n, r) {
            var i, s;
            if (e && e.preventDefault && e.handleObj) {
                i = e.handleObj;
                w(e.delegateTarget).off(i.namespace ? i.origType + "." + i.namespace : i.origType, i.selector, i.handler);
                return this;
            }
            if (typeof e == "object") {
                for (s in e) this.off(s, n, e[s]);
                return this;
            }
            if (n === !1 || typeof n == "function") {
                r = n;
                n = t;
            }
            r === !1 && (r = st);
            return this.each(function() {
                w.event.remove(this, e, r, n);
            });
        },
        trigger: function(e, t) {
            return this.each(function() {
                w.event.trigger(e, t, this);
            });
        },
        triggerHandler: function(e, t) {
            var n = this[0];
            if (n) return w.event.trigger(e, t, n, !0);
        }
    });
    var ut = /^.[^:#\[\.,]*$/, at = /^(?:parents|prev(?:Until|All))/, ft = w.expr.match.needsContext, lt = {
        children: !0,
        contents: !0,
        next: !0,
        prev: !0
    };
    w.fn.extend({
        find: function(e) {
            var t, n = [], r = this, i = r.length;
            if (typeof e != "string") return this.pushStack(w(e).filter(function() {
                for (t = 0; t < i; t++) if (w.contains(r[t], this)) return !0;
            }));
            for (t = 0; t < i; t++) w.find(e, r[t], n);
            n = this.pushStack(i > 1 ? w.unique(n) : n);
            n.selector = this.selector ? this.selector + " " + e : e;
            return n;
        },
        has: function(e) {
            var t, n = w(e, this), r = n.length;
            return this.filter(function() {
                for (t = 0; t < r; t++) if (w.contains(this, n[t])) return !0;
            });
        },
        not: function(e) {
            return this.pushStack(ht(this, e || [], !0));
        },
        filter: function(e) {
            return this.pushStack(ht(this, e || [], !1));
        },
        is: function(e) {
            return !!ht(this, typeof e == "string" && ft.test(e) ? w(e) : e || [], !1).length;
        },
        closest: function(e, t) {
            var n, r = 0, i = this.length, s = [], o = ft.test(e) || typeof e != "string" ? w(e, t || this.context) : 0;
            for (; r < i; r++) for (n = this[r]; n && n !== t; n = n.parentNode) if (n.nodeType < 11 && (o ? o.index(n) > -1 : n.nodeType === 1 && w.find.matchesSelector(n, e))) {
                n = s.push(n);
                break;
            }
            return this.pushStack(s.length > 1 ? w.unique(s) : s);
        },
        index: function(e) {
            return e ? typeof e == "string" ? w.inArray(this[0], w(e)) : w.inArray(e.jquery ? e[0] : e, this) : this[0] && this[0].parentNode ? this.first().prevAll().length : -1;
        },
        add: function(e, t) {
            var n = typeof e == "string" ? w(e, t) : w.makeArray(e && e.nodeType ? [ e ] : e), r = w.merge(this.get(), n);
            return this.pushStack(w.unique(r));
        },
        addBack: function(e) {
            return this.add(e == null ? this.prevObject : this.prevObject.filter(e));
        }
    });
    w.each({
        parent: function(e) {
            var t = e.parentNode;
            return t && t.nodeType !== 11 ? t : null;
        },
        parents: function(e) {
            return w.dir(e, "parentNode");
        },
        parentsUntil: function(e, t, n) {
            return w.dir(e, "parentNode", n);
        },
        next: function(e) {
            return ct(e, "nextSibling");
        },
        prev: function(e) {
            return ct(e, "previousSibling");
        },
        nextAll: function(e) {
            return w.dir(e, "nextSibling");
        },
        prevAll: function(e) {
            return w.dir(e, "previousSibling");
        },
        nextUntil: function(e, t, n) {
            return w.dir(e, "nextSibling", n);
        },
        prevUntil: function(e, t, n) {
            return w.dir(e, "previousSibling", n);
        },
        siblings: function(e) {
            return w.sibling((e.parentNode || {}).firstChild, e);
        },
        children: function(e) {
            return w.sibling(e.firstChild);
        },
        contents: function(e) {
            return w.nodeName(e, "iframe") ? e.contentDocument || e.contentWindow.document : w.merge([], e.childNodes);
        }
    }, function(e, t) {
        w.fn[e] = function(n, r) {
            var i = w.map(this, t, n);
            e.slice(-5) !== "Until" && (r = n);
            r && typeof r == "string" && (i = w.filter(r, i));
            if (this.length > 1) {
                lt[e] || (i = w.unique(i));
                at.test(e) && (i = i.reverse());
            }
            return this.pushStack(i);
        };
    });
    w.extend({
        filter: function(e, t, n) {
            var r = t[0];
            n && (e = ":not(" + e + ")");
            return t.length === 1 && r.nodeType === 1 ? w.find.matchesSelector(r, e) ? [ r ] : [] : w.find.matches(e, w.grep(t, function(e) {
                return e.nodeType === 1;
            }));
        },
        dir: function(e, n, r) {
            var i = [], s = e[n];
            while (s && s.nodeType !== 9 && (r === t || s.nodeType !== 1 || !w(s).is(r))) {
                s.nodeType === 1 && i.push(s);
                s = s[n];
            }
            return i;
        },
        sibling: function(e, t) {
            var n = [];
            for (; e; e = e.nextSibling) e.nodeType === 1 && e !== t && n.push(e);
            return n;
        }
    });
    var dt = "abbr|article|aside|audio|bdi|canvas|data|datalist|details|figcaption|figure|footer|header|hgroup|mark|meter|nav|output|progress|section|summary|time|video", vt = / jQuery\d+="(?:null|\d+)"/g, mt = new RegExp("<(?:" + dt + ")[\\s/>]", "i"), gt = /^\s+/, yt = /<(?!area|br|col|embed|hr|img|input|link|meta|param)(([\w:]+)[^>]*)\/>/gi, bt = /<([\w:]+)/, wt = /<tbody/i, Et = /<|&#?\w+;/, St = /<(?:script|style|link)/i, xt = /^(?:checkbox|radio)$/i, Tt = /checked\s*(?:[^=]|=\s*.checked.)/i, Nt = /^$|\/(?:java|ecma)script/i, Ct = /^true\/(.*)/, kt = /^\s*<!(?:\[CDATA\[|--)|(?:\]\]|--)>\s*$/g, Lt = {
        option: [ 1, "<select multiple='multiple'>", "</select>" ],
        legend: [ 1, "<fieldset>", "</fieldset>" ],
        area: [ 1, "<map>", "</map>" ],
        param: [ 1, "<object>", "</object>" ],
        thead: [ 1, "<table>", "</table>" ],
        tr: [ 2, "<table><tbody>", "</tbody></table>" ],
        col: [ 2, "<table><tbody></tbody><colgroup>", "</colgroup></table>" ],
        td: [ 3, "<table><tbody><tr>", "</tr></tbody></table>" ],
        _default: w.support.htmlSerialize ? [ 0, "", "" ] : [ 1, "X<div>", "</div>" ]
    }, At = pt(o), Ot = At.appendChild(o.createElement("div"));
    Lt.optgroup = Lt.option;
    Lt.tbody = Lt.tfoot = Lt.colgroup = Lt.caption = Lt.thead;
    Lt.th = Lt.td;
    w.fn.extend({
        text: function(e) {
            return w.access(this, function(e) {
                return e === t ? w.text(this) : this.empty().append((this[0] && this[0].ownerDocument || o).createTextNode(e));
            }, null, e, arguments.length);
        },
        append: function() {
            return this.domManip(arguments, function(e) {
                if (this.nodeType === 1 || this.nodeType === 11 || this.nodeType === 9) {
                    var t = Mt(this, e);
                    t.appendChild(e);
                }
            });
        },
        prepend: function() {
            return this.domManip(arguments, function(e) {
                if (this.nodeType === 1 || this.nodeType === 11 || this.nodeType === 9) {
                    var t = Mt(this, e);
                    t.insertBefore(e, t.firstChild);
                }
            });
        },
        before: function() {
            return this.domManip(arguments, function(e) {
                this.parentNode && this.parentNode.insertBefore(e, this);
            });
        },
        after: function() {
            return this.domManip(arguments, function(e) {
                this.parentNode && this.parentNode.insertBefore(e, this.nextSibling);
            });
        },
        remove: function(e, t) {
            var n, r = e ? w.filter(e, this) : this, i = 0;
            for (; (n = r[i]) != null; i++) {
                !t && n.nodeType === 1 && w.cleanData(jt(n));
                if (n.parentNode) {
                    t && w.contains(n.ownerDocument, n) && Pt(jt(n, "script"));
                    n.parentNode.removeChild(n);
                }
            }
            return this;
        },
        empty: function() {
            var e, t = 0;
            for (; (e = this[t]) != null; t++) {
                e.nodeType === 1 && w.cleanData(jt(e, !1));
                while (e.firstChild) e.removeChild(e.firstChild);
                e.options && w.nodeName(e, "select") && (e.options.length = 0);
            }
            return this;
        },
        clone: function(e, t) {
            e = e == null ? !1 : e;
            t = t == null ? e : t;
            return this.map(function() {
                return w.clone(this, e, t);
            });
        },
        html: function(e) {
            return w.access(this, function(e) {
                var n = this[0] || {}, r = 0, i = this.length;
                if (e === t) return n.nodeType === 1 ? n.innerHTML.replace(vt, "") : t;
                if (typeof e == "string" && !St.test(e) && (w.support.htmlSerialize || !mt.test(e)) && (w.support.leadingWhitespace || !gt.test(e)) && !Lt[(bt.exec(e) || [ "", "" ])[1].toLowerCase()]) {
                    e = e.replace(yt, "<$1></$2>");
                    try {
                        for (; r < i; r++) {
                            n = this[r] || {};
                            if (n.nodeType === 1) {
                                w.cleanData(jt(n, !1));
                                n.innerHTML = e;
                            }
                        }
                        n = 0;
                    } catch (s) {}
                }
                n && this.empty().append(e);
            }, null, e, arguments.length);
        },
        replaceWith: function() {
            var e = w.map(this, function(e) {
                return [ e.nextSibling, e.parentNode ];
            }), t = 0;
            this.domManip(arguments, function(n) {
                var r = e[t++], i = e[t++];
                if (i) {
                    r && r.parentNode !== i && (r = this.nextSibling);
                    w(this).remove();
                    i.insertBefore(n, r);
                }
            }, !0);
            return t ? this : this.remove();
        },
        detach: function(e) {
            return this.remove(e, !0);
        },
        domManip: function(e, t, n) {
            e = p.apply([], e);
            var r, i, s, o, u, a, f = 0, l = this.length, c = this, h = l - 1, d = e[0], v = w.isFunction(d);
            if (v || !(l <= 1 || typeof d != "string" || w.support.checkClone || !Tt.test(d))) return this.each(function(r) {
                var i = c.eq(r);
                v && (e[0] = d.call(this, r, i.html()));
                i.domManip(e, t, n);
            });
            if (l) {
                a = w.buildFragment(e, this[0].ownerDocument, !1, !n && this);
                r = a.firstChild;
                a.childNodes.length === 1 && (a = r);
                if (r) {
                    o = w.map(jt(a, "script"), _t);
                    s = o.length;
                    for (; f < l; f++) {
                        i = a;
                        if (f !== h) {
                            i = w.clone(i, !0, !0);
                            s && w.merge(o, jt(i, "script"));
                        }
                        t.call(this[f], i, f);
                    }
                    if (s) {
                        u = o[o.length - 1].ownerDocument;
                        w.map(o, Dt);
                        for (f = 0; f < s; f++) {
                            i = o[f];
                            Nt.test(i.type || "") && !w._data(i, "globalEval") && w.contains(u, i) && (i.src ? w._evalUrl(i.src) : w.globalEval((i.text || i.textContent || i.innerHTML || "").replace(kt, "")));
                        }
                    }
                    a = r = null;
                }
            }
            return this;
        }
    });
    w.each({
        appendTo: "append",
        prependTo: "prepend",
        insertBefore: "before",
        insertAfter: "after",
        replaceAll: "replaceWith"
    }, function(e, t) {
        w.fn[e] = function(e) {
            var n, r = 0, i = [], s = w(e), o = s.length - 1;
            for (; r <= o; r++) {
                n = r === o ? this : this.clone(!0);
                w(s[r])[t](n);
                d.apply(i, n.get());
            }
            return this.pushStack(i);
        };
    });
    w.extend({
        clone: function(e, t, n) {
            var r, i, s, o, u, a = w.contains(e.ownerDocument, e);
            if (w.support.html5Clone || w.isXMLDoc(e) || !mt.test("<" + e.nodeName + ">")) s = e.cloneNode(!0); else {
                Ot.innerHTML = e.outerHTML;
                Ot.removeChild(s = Ot.firstChild);
            }
            if ((!w.support.noCloneEvent || !w.support.noCloneChecked) && (e.nodeType === 1 || e.nodeType === 11) && !w.isXMLDoc(e)) {
                r = jt(s);
                u = jt(e);
                for (o = 0; (i = u[o]) != null; ++o) r[o] && Bt(i, r[o]);
            }
            if (t) if (n) {
                u = u || jt(e);
                r = r || jt(s);
                for (o = 0; (i = u[o]) != null; o++) Ht(i, r[o]);
            } else Ht(e, s);
            r = jt(s, "script");
            r.length > 0 && Pt(r, !a && jt(e, "script"));
            r = u = i = null;
            return s;
        },
        buildFragment: function(e, t, n, r) {
            var i, s, o, u, a, f, l, c = e.length, h = pt(t), p = [], d = 0;
            for (; d < c; d++) {
                s = e[d];
                if (s || s === 0) if (w.type(s) === "object") w.merge(p, s.nodeType ? [ s ] : s); else if (!Et.test(s)) p.push(t.createTextNode(s)); else {
                    u = u || h.appendChild(t.createElement("div"));
                    a = (bt.exec(s) || [ "", "" ])[1].toLowerCase();
                    l = Lt[a] || Lt._default;
                    u.innerHTML = l[1] + s.replace(yt, "<$1></$2>") + l[2];
                    i = l[0];
                    while (i--) u = u.lastChild;
                    !w.support.leadingWhitespace && gt.test(s) && p.push(t.createTextNode(gt.exec(s)[0]));
                    if (!w.support.tbody) {
                        s = a === "table" && !wt.test(s) ? u.firstChild : l[1] === "<table>" && !wt.test(s) ? u : 0;
                        i = s && s.childNodes.length;
                        while (i--) w.nodeName(f = s.childNodes[i], "tbody") && !f.childNodes.length && s.removeChild(f);
                    }
                    w.merge(p, u.childNodes);
                    u.textContent = "";
                    while (u.firstChild) u.removeChild(u.firstChild);
                    u = h.lastChild;
                }
            }
            u && h.removeChild(u);
            w.support.appendChecked || w.grep(jt(p, "input"), Ft);
            d = 0;
            while (s = p[d++]) {
                if (r && w.inArray(s, r) !== -1) continue;
                o = w.contains(s.ownerDocument, s);
                u = jt(h.appendChild(s), "script");
                o && Pt(u);
                if (n) {
                    i = 0;
                    while (s = u[i++]) Nt.test(s.type || "") && n.push(s);
                }
            }
            u = null;
            return h;
        },
        cleanData: function(e, t) {
            var n, r, s, o, u = 0, a = w.expando, f = w.cache, l = w.support.deleteExpando, h = w.event.special;
            for (; (n = e[u]) != null; u++) if (t || w.acceptData(n)) {
                s = n[a];
                o = s && f[s];
                if (o) {
                    if (o.events) for (r in o.events) h[r] ? w.event.remove(n, r) : w.removeEvent(n, r, o.handle);
                    if (f[s]) {
                        delete f[s];
                        l ? delete n[a] : typeof n.removeAttribute !== i ? n.removeAttribute(a) : n[a] = null;
                        c.push(s);
                    }
                }
            }
        },
        _evalUrl: function(e) {
            return w.ajax({
                url: e,
                type: "GET",
                dataType: "script",
                async: !1,
                global: !1,
                "throws": !0
            });
        }
    });
    w.fn.extend({
        wrapAll: function(e) {
            if (w.isFunction(e)) return this.each(function(t) {
                w(this).wrapAll(e.call(this, t));
            });
            if (this[0]) {
                var t = w(e, this[0].ownerDocument).eq(0).clone(!0);
                this[0].parentNode && t.insertBefore(this[0]);
                t.map(function() {
                    var e = this;
                    while (e.firstChild && e.firstChild.nodeType === 1) e = e.firstChild;
                    return e;
                }).append(this);
            }
            return this;
        },
        wrapInner: function(e) {
            return w.isFunction(e) ? this.each(function(t) {
                w(this).wrapInner(e.call(this, t));
            }) : this.each(function() {
                var t = w(this), n = t.contents();
                n.length ? n.wrapAll(e) : t.append(e);
            });
        },
        wrap: function(e) {
            var t = w.isFunction(e);
            return this.each(function(n) {
                w(this).wrapAll(t ? e.call(this, n) : e);
            });
        },
        unwrap: function() {
            return this.parent().each(function() {
                w.nodeName(this, "body") || w(this).replaceWith(this.childNodes);
            }).end();
        }
    });
    var It, qt, Rt, Ut = /alpha\([^)]*\)/i, zt = /opacity\s*=\s*([^)]*)/, Wt = /^(top|right|bottom|left)$/, Xt = /^(none|table(?!-c[ea]).+)/, Vt = /^margin/, $t = new RegExp("^(" + E + ")(.*)$", "i"), Jt = new RegExp("^(" + E + ")(?!px)[a-z%]+$", "i"), Kt = new RegExp("^([+-])=(" + E + ")", "i"), Qt = {
        BODY: "block"
    }, Gt = {
        position: "absolute",
        visibility: "hidden",
        display: "block"
    }, Yt = {
        letterSpacing: 0,
        fontWeight: 400
    }, Zt = [ "Top", "Right", "Bottom", "Left" ], en = [ "Webkit", "O", "Moz", "ms" ];
    w.fn.extend({
        css: function(e, n) {
            return w.access(this, function(e, n, r) {
                var i, s, o = {}, u = 0;
                if (w.isArray(n)) {
                    s = qt(e);
                    i = n.length;
                    for (; u < i; u++) o[n[u]] = w.css(e, n[u], !1, s);
                    return o;
                }
                return r !== t ? w.style(e, n, r) : w.css(e, n);
            }, e, n, arguments.length > 1);
        },
        show: function() {
            return rn(this, !0);
        },
        hide: function() {
            return rn(this);
        },
        toggle: function(e) {
            var t = typeof e == "boolean";
            return this.each(function() {
                (t ? e : nn(this)) ? w(this).show() : w(this).hide();
            });
        }
    });
    w.extend({
        cssHooks: {
            opacity: {
                get: function(e, t) {
                    if (t) {
                        var n = Rt(e, "opacity");
                        return n === "" ? "1" : n;
                    }
                }
            }
        },
        cssNumber: {
            columnCount: !0,
            fillOpacity: !0,
            fontWeight: !0,
            lineHeight: !0,
            opacity: !0,
            orphans: !0,
            widows: !0,
            zIndex: !0,
            zoom: !0
        },
        cssProps: {
            "float": w.support.cssFloat ? "cssFloat" : "styleFloat"
        },
        style: function(e, n, r, i) {
            if (!e || e.nodeType === 3 || e.nodeType === 8 || !e.style) return;
            var s, o, u, a = w.camelCase(n), f = e.style;
            n = w.cssProps[a] || (w.cssProps[a] = tn(f, a));
            u = w.cssHooks[n] || w.cssHooks[a];
            if (r === t) return u && "get" in u && (s = u.get(e, !1, i)) !== t ? s : f[n];
            o = typeof r;
            if (o === "string" && (s = Kt.exec(r))) {
                r = (s[1] + 1) * s[2] + parseFloat(w.css(e, n));
                o = "number";
            }
            if (r == null || o === "number" && isNaN(r)) return;
            o === "number" && !w.cssNumber[a] && (r += "px");
            !w.support.clearCloneStyle && r === "" && n.indexOf("background") === 0 && (f[n] = "inherit");
            if (!u || !("set" in u) || (r = u.set(e, r, i)) !== t) try {
                f[n] = r;
            } catch (l) {}
        },
        css: function(e, n, r, i) {
            var s, o, u, a = w.camelCase(n);
            n = w.cssProps[a] || (w.cssProps[a] = tn(e.style, a));
            u = w.cssHooks[n] || w.cssHooks[a];
            u && "get" in u && (o = u.get(e, !0, r));
            o === t && (o = Rt(e, n, i));
            o === "normal" && n in Yt && (o = Yt[n]);
            if (r === "" || r) {
                s = parseFloat(o);
                return r === !0 || w.isNumeric(s) ? s || 0 : o;
            }
            return o;
        }
    });
    if (e.getComputedStyle) {
        qt = function(t) {
            return e.getComputedStyle(t, null);
        };
        Rt = function(e, n, r) {
            var i, s, o, u = r || qt(e), a = u ? u.getPropertyValue(n) || u[n] : t, f = e.style;
            if (u) {
                a === "" && !w.contains(e.ownerDocument, e) && (a = w.style(e, n));
                if (Jt.test(a) && Vt.test(n)) {
                    i = f.width;
                    s = f.minWidth;
                    o = f.maxWidth;
                    f.minWidth = f.maxWidth = f.width = a;
                    a = u.width;
                    f.width = i;
                    f.minWidth = s;
                    f.maxWidth = o;
                }
            }
            return a;
        };
    } else if (o.documentElement.currentStyle) {
        qt = function(e) {
            return e.currentStyle;
        };
        Rt = function(e, n, r) {
            var i, s, o, u = r || qt(e), a = u ? u[n] : t, f = e.style;
            a == null && f && f[n] && (a = f[n]);
            if (Jt.test(a) && !Wt.test(n)) {
                i = f.left;
                s = e.runtimeStyle;
                o = s && s.left;
                o && (s.left = e.currentStyle.left);
                f.left = n === "fontSize" ? "1em" : a;
                a = f.pixelLeft + "px";
                f.left = i;
                o && (s.left = o);
            }
            return a === "" ? "auto" : a;
        };
    }
    w.each([ "height", "width" ], function(e, t) {
        w.cssHooks[t] = {
            get: function(e, n, r) {
                if (n) return e.offsetWidth === 0 && Xt.test(w.css(e, "display")) ? w.swap(e, Gt, function() {
                    return un(e, t, r);
                }) : un(e, t, r);
            },
            set: function(e, n, r) {
                var i = r && qt(e);
                return sn(e, n, r ? on(e, t, r, w.support.boxSizing && w.css(e, "boxSizing", !1, i) === "border-box", i) : 0);
            }
        };
    });
    w.support.opacity || (w.cssHooks.opacity = {
        get: function(e, t) {
            return zt.test((t && e.currentStyle ? e.currentStyle.filter : e.style.filter) || "") ? .01 * parseFloat(RegExp.$1) + "" : t ? "1" : "";
        },
        set: function(e, t) {
            var n = e.style, r = e.currentStyle, i = w.isNumeric(t) ? "alpha(opacity=" + t * 100 + ")" : "", s = r && r.filter || n.filter || "";
            n.zoom = 1;
            if ((t >= 1 || t === "") && w.trim(s.replace(Ut, "")) === "" && n.removeAttribute) {
                n.removeAttribute("filter");
                if (t === "" || r && !r.filter) return;
            }
            n.filter = Ut.test(s) ? s.replace(Ut, i) : s + " " + i;
        }
    });
    w(function() {
        w.support.reliableMarginRight || (w.cssHooks.marginRight = {
            get: function(e, t) {
                if (t) return w.swap(e, {
                    display: "inline-block"
                }, Rt, [ e, "marginRight" ]);
            }
        });
        !w.support.pixelPosition && w.fn.position && w.each([ "top", "left" ], function(e, t) {
            w.cssHooks[t] = {
                get: function(e, n) {
                    if (n) {
                        n = Rt(e, t);
                        return Jt.test(n) ? w(e).position()[t] + "px" : n;
                    }
                }
            };
        });
    });
    if (w.expr && w.expr.filters) {
        w.expr.filters.hidden = function(e) {
            return e.offsetWidth <= 0 && e.offsetHeight <= 0 || !w.support.reliableHiddenOffsets && (e.style && e.style.display || w.css(e, "display")) === "none";
        };
        w.expr.filters.visible = function(e) {
            return !w.expr.filters.hidden(e);
        };
    }
    w.each({
        margin: "",
        padding: "",
        border: "Width"
    }, function(e, t) {
        w.cssHooks[e + t] = {
            expand: function(n) {
                var r = 0, i = {}, s = typeof n == "string" ? n.split(" ") : [ n ];
                for (; r < 4; r++) i[e + Zt[r] + t] = s[r] || s[r - 2] || s[0];
                return i;
            }
        };
        Vt.test(e) || (w.cssHooks[e + t].set = sn);
    });
    var ln = /%20/g, cn = /\[\]$/, hn = /\r?\n/g, pn = /^(?:submit|button|image|reset|file)$/i, dn = /^(?:input|select|textarea|keygen)/i;
    w.fn.extend({
        serialize: function() {
            return w.param(this.serializeArray());
        },
        serializeArray: function() {
            return this.map(function() {
                var e = w.prop(this, "elements");
                return e ? w.makeArray(e) : this;
            }).filter(function() {
                var e = this.type;
                return this.name && !w(this).is(":disabled") && dn.test(this.nodeName) && !pn.test(e) && (this.checked || !xt.test(e));
            }).map(function(e, t) {
                var n = w(this).val();
                return n == null ? null : w.isArray(n) ? w.map(n, function(e) {
                    return {
                        name: t.name,
                        value: e.replace(hn, "\r\n")
                    };
                }) : {
                    name: t.name,
                    value: n.replace(hn, "\r\n")
                };
            }).get();
        }
    });
    w.param = function(e, n) {
        var r, i = [], s = function(e, t) {
            t = w.isFunction(t) ? t() : t == null ? "" : t;
            i[i.length] = encodeURIComponent(e) + "=" + encodeURIComponent(t);
        };
        n === t && (n = w.ajaxSettings && w.ajaxSettings.traditional);
        if (w.isArray(e) || e.jquery && !w.isPlainObject(e)) w.each(e, function() {
            s(this.name, this.value);
        }); else for (r in e) vn(r, e[r], n, s);
        return i.join("&").replace(ln, "+");
    };
    w.each("blur focus focusin focusout load resize scroll unload click dblclick mousedown mouseup mousemove mouseover mouseout mouseenter mouseleave change select submit keydown keypress keyup error contextmenu".split(" "), function(e, t) {
        w.fn[t] = function(e, n) {
            return arguments.length > 0 ? this.on(t, null, e, n) : this.trigger(t);
        };
    });
    w.fn.extend({
        hover: function(e, t) {
            return this.mouseenter(e).mouseleave(t || e);
        },
        bind: function(e, t, n) {
            return this.on(e, null, t, n);
        },
        unbind: function(e, t) {
            return this.off(e, null, t);
        },
        delegate: function(e, t, n, r) {
            return this.on(t, e, n, r);
        },
        undelegate: function(e, t, n) {
            return arguments.length === 1 ? this.off(e, "**") : this.off(t, e || "**", n);
        }
    });
    var mn, gn, yn = w.now(), bn = /\?/, wn = /#.*$/, En = /([?&])_=[^&]*/, Sn = /^(.*?):[ \t]*([^\r\n]*)\r?$/mg, xn = /^(?:about|app|app-storage|.+-extension|file|res|widget):$/, Tn = /^(?:GET|HEAD)$/, Nn = /^\/\//, Cn = /^([\w.+-]+:)(?:\/\/([^\/?#:]*)(?::(\d+)|)|)/, kn = w.fn.load, Ln = {}, An = {}, On = "*/".concat("*");
    try {
        gn = s.href;
    } catch (Mn) {
        gn = o.createElement("a");
        gn.href = "";
        gn = gn.href;
    }
    mn = Cn.exec(gn.toLowerCase()) || [];
    w.fn.load = function(e, n, r) {
        if (typeof e != "string" && kn) return kn.apply(this, arguments);
        var i, s, o, u = this, a = e.indexOf(" ");
        if (a >= 0) {
            i = e.slice(a, e.length);
            e = e.slice(0, a);
        }
        if (w.isFunction(n)) {
            r = n;
            n = t;
        } else n && typeof n == "object" && (o = "POST");
        u.length > 0 && w.ajax({
            url: e,
            type: o,
            dataType: "html",
            data: n
        }).done(function(e) {
            s = arguments;
            u.html(i ? w("<div>").append(w.parseHTML(e)).find(i) : e);
        }).complete(r && function(e, t) {
            u.each(r, s || [ e.responseText, t, e ]);
        });
        return this;
    };
    w.each([ "ajaxStart", "ajaxStop", "ajaxComplete", "ajaxError", "ajaxSuccess", "ajaxSend" ], function(e, t) {
        w.fn[t] = function(e) {
            return this.on(t, e);
        };
    });
    w.extend({
        active: 0,
        lastModified: {},
        etag: {},
        ajaxSettings: {
            url: gn,
            type: "GET",
            isLocal: xn.test(mn[1]),
            global: !0,
            processData: !0,
            async: !0,
            contentType: "application/x-www-form-urlencoded; charset=UTF-8",
            accepts: {
                "*": On,
                text: "text/plain",
                html: "text/html",
                xml: "application/xml, text/xml",
                json: "application/json, text/javascript"
            },
            contents: {
                xml: /xml/,
                html: /html/,
                json: /json/
            },
            responseFields: {
                xml: "responseXML",
                text: "responseText",
                json: "responseJSON"
            },
            converters: {
                "* text": String,
                "text html": !0,
                "text json": w.parseJSON,
                "text xml": w.parseXML
            },
            flatOptions: {
                url: !0,
                context: !0
            }
        },
        ajaxSetup: function(e, t) {
            return t ? Pn(Pn(e, w.ajaxSettings), t) : Pn(w.ajaxSettings, e);
        },
        ajaxPrefilter: _n(Ln),
        ajaxTransport: _n(An),
        ajax: function(e, n) {
            function N(e, n, r, i) {
                var l, g, y, E, S, T = n;
                if (b === 2) return;
                b = 2;
                u && clearTimeout(u);
                f = t;
                o = i || "";
                x.readyState = e > 0 ? 4 : 0;
                l = e >= 200 && e < 300 || e === 304;
                r && (E = Hn(c, x, r));
                E = Bn(c, E, x, l);
                if (l) {
                    if (c.ifModified) {
                        S = x.getResponseHeader("Last-Modified");
                        S && (w.lastModified[s] = S);
                        S = x.getResponseHeader("etag");
                        S && (w.etag[s] = S);
                    }
                    if (e === 204 || c.type === "HEAD") T = "nocontent"; else if (e === 304) T = "notmodified"; else {
                        T = E.state;
                        g = E.data;
                        y = E.error;
                        l = !y;
                    }
                } else {
                    y = T;
                    if (e || !T) {
                        T = "error";
                        e < 0 && (e = 0);
                    }
                }
                x.status = e;
                x.statusText = (n || T) + "";
                l ? d.resolveWith(h, [ g, T, x ]) : d.rejectWith(h, [ x, T, y ]);
                x.statusCode(m);
                m = t;
                a && p.trigger(l ? "ajaxSuccess" : "ajaxError", [ x, c, l ? g : y ]);
                v.fireWith(h, [ x, T ]);
                if (a) {
                    p.trigger("ajaxComplete", [ x, c ]);
                    --w.active || w.event.trigger("ajaxStop");
                }
            }
            if (typeof e == "object") {
                n = e;
                e = t;
            }
            n = n || {};
            var r, i, s, o, u, a, f, l, c = w.ajaxSetup({}, n), h = c.context || c, p = c.context && (h.nodeType || h.jquery) ? w(h) : w.event, d = w.Deferred(), v = w.Callbacks("once memory"), m = c.statusCode || {}, g = {}, y = {}, b = 0, E = "canceled", x = {
                readyState: 0,
                getResponseHeader: function(e) {
                    var t;
                    if (b === 2) {
                        if (!l) {
                            l = {};
                            while (t = Sn.exec(o)) l[t[1].toLowerCase()] = t[2];
                        }
                        t = l[e.toLowerCase()];
                    }
                    return t == null ? null : t;
                },
                getAllResponseHeaders: function() {
                    return b === 2 ? o : null;
                },
                setRequestHeader: function(e, t) {
                    var n = e.toLowerCase();
                    if (!b) {
                        e = y[n] = y[n] || e;
                        g[e] = t;
                    }
                    return this;
                },
                overrideMimeType: function(e) {
                    b || (c.mimeType = e);
                    return this;
                },
                statusCode: function(e) {
                    var t;
                    if (e) if (b < 2) for (t in e) m[t] = [ m[t], e[t] ]; else x.always(e[x.status]);
                    return this;
                },
                abort: function(e) {
                    var t = e || E;
                    f && f.abort(t);
                    N(0, t);
                    return this;
                }
            };
            d.promise(x).complete = v.add;
            x.success = x.done;
            x.error = x.fail;
            c.url = ((e || c.url || gn) + "").replace(wn, "").replace(Nn, mn[1] + "//");
            c.type = n.method || n.type || c.method || c.type;
            c.dataTypes = w.trim(c.dataType || "*").toLowerCase().match(S) || [ "" ];
            if (c.crossDomain == null) {
                r = Cn.exec(c.url.toLowerCase());
                c.crossDomain = !(!r || r[1] === mn[1] && r[2] === mn[2] && (r[3] || (r[1] === "http:" ? "80" : "443")) === (mn[3] || (mn[1] === "http:" ? "80" : "443")));
            }
            c.data && c.processData && typeof c.data != "string" && (c.data = w.param(c.data, c.traditional));
            Dn(Ln, c, n, x);
            if (b === 2) return x;
            a = c.global;
            a && w.active++ === 0 && w.event.trigger("ajaxStart");
            c.type = c.type.toUpperCase();
            c.hasContent = !Tn.test(c.type);
            s = c.url;
            if (!c.hasContent) {
                if (c.data) {
                    s = c.url += (bn.test(s) ? "&" : "?") + c.data;
                    delete c.data;
                }
                c.cache === !1 && (c.url = En.test(s) ? s.replace(En, "$1_=" + yn++) : s + (bn.test(s) ? "&" : "?") + "_=" + yn++);
            }
            if (c.ifModified) {
                w.lastModified[s] && x.setRequestHeader("If-Modified-Since", w.lastModified[s]);
                w.etag[s] && x.setRequestHeader("If-None-Match", w.etag[s]);
            }
            (c.data && c.hasContent && c.contentType !== !1 || n.contentType) && x.setRequestHeader("Content-Type", c.contentType);
            x.setRequestHeader("Accept", c.dataTypes[0] && c.accepts[c.dataTypes[0]] ? c.accepts[c.dataTypes[0]] + (c.dataTypes[0] !== "*" ? ", " + On + "; q=0.01" : "") : c.accepts["*"]);
            for (i in c.headers) x.setRequestHeader(i, c.headers[i]);
            if (!c.beforeSend || c.beforeSend.call(h, x, c) !== !1 && b !== 2) {
                E = "abort";
                for (i in {
                    success: 1,
                    error: 1,
                    complete: 1
                }) x[i](c[i]);
                f = Dn(An, c, n, x);
                if (!f) N(-1, "No Transport"); else {
                    x.readyState = 1;
                    a && p.trigger("ajaxSend", [ x, c ]);
                    c.async && c.timeout > 0 && (u = setTimeout(function() {
                        x.abort("timeout");
                    }, c.timeout));
                    try {
                        b = 1;
                        f.send(g, N);
                    } catch (T) {
                        if (!(b < 2)) throw T;
                        N(-1, T);
                    }
                }
                return x;
            }
            return x.abort();
        },
        getJSON: function(e, t, n) {
            return w.get(e, t, n, "json");
        },
        getScript: function(e, n) {
            return w.get(e, t, n, "script");
        }
    });
    w.each([ "get", "post" ], function(e, n) {
        w[n] = function(e, r, i, s) {
            if (w.isFunction(r)) {
                s = s || i;
                i = r;
                r = t;
            }
            return w.ajax({
                url: e,
                type: n,
                dataType: s,
                data: r,
                success: i
            });
        };
    });
    w.ajaxSetup({
        accepts: {
            script: "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript"
        },
        contents: {
            script: /(?:java|ecma)script/
        },
        converters: {
            "text script": function(e) {
                w.globalEval(e);
                return e;
            }
        }
    });
    w.ajaxPrefilter("script", function(e) {
        e.cache === t && (e.cache = !1);
        if (e.crossDomain) {
            e.type = "GET";
            e.global = !1;
        }
    });
    w.ajaxTransport("script", function(e) {
        if (e.crossDomain) {
            var n, r = o.head || w("head")[0] || o.documentElement;
            return {
                send: function(t, i) {
                    n = o.createElement("script");
                    n.async = !0;
                    e.scriptCharset && (n.charset = e.scriptCharset);
                    n.src = e.url;
                    n.onload = n.onreadystatechange = function(e, t) {
                        if (t || !n.readyState || /loaded|complete/.test(n.readyState)) {
                            n.onload = n.onreadystatechange = null;
                            n.parentNode && n.parentNode.removeChild(n);
                            n = null;
                            t || i(200, "success");
                        }
                    };
                    r.insertBefore(n, r.firstChild);
                },
                abort: function() {
                    n && n.onload(t, !0);
                }
            };
        }
    });
    var jn = [], Fn = /(=)\?(?=&|$)|\?\?/;
    w.ajaxSetup({
        jsonp: "callback",
        jsonpCallback: function() {
            var e = jn.pop() || w.expando + "_" + yn++;
            this[e] = !0;
            return e;
        }
    });
    w.ajaxPrefilter("json jsonp", function(n, r, i) {
        var s, o, u, a = n.jsonp !== !1 && (Fn.test(n.url) ? "url" : typeof n.data == "string" && !(n.contentType || "").indexOf("application/x-www-form-urlencoded") && Fn.test(n.data) && "data");
        if (a || n.dataTypes[0] === "jsonp") {
            s = n.jsonpCallback = w.isFunction(n.jsonpCallback) ? n.jsonpCallback() : n.jsonpCallback;
            a ? n[a] = n[a].replace(Fn, "$1" + s) : n.jsonp !== !1 && (n.url += (bn.test(n.url) ? "&" : "?") + n.jsonp + "=" + s);
            n.converters["script json"] = function() {
                u || w.error(s + " was not called");
                return u[0];
            };
            n.dataTypes[0] = "json";
            o = e[s];
            e[s] = function() {
                u = arguments;
            };
            i.always(function() {
                e[s] = o;
                if (n[s]) {
                    n.jsonpCallback = r.jsonpCallback;
                    jn.push(s);
                }
                u && w.isFunction(o) && o(u[0]);
                u = o = t;
            });
            return "script";
        }
    });
    var In, qn, Rn = 0, Un = e.ActiveXObject && function() {
        var e;
        for (e in In) In[e](t, !0);
    };
    w.ajaxSettings.xhr = e.ActiveXObject ? function() {
        return !this.isLocal && zn() || Wn();
    } : zn;
    qn = w.ajaxSettings.xhr();
    w.support.cors = !!qn && "withCredentials" in qn;
    qn = w.support.ajax = !!qn;
    qn && w.ajaxTransport(function(n) {
        if (!n.crossDomain || w.support.cors) {
            var r;
            return {
                send: function(i, s) {
                    var o, u, a = n.xhr();
                    n.username ? a.open(n.type, n.url, n.async, n.username, n.password) : a.open(n.type, n.url, n.async);
                    if (n.xhrFields) for (u in n.xhrFields) a[u] = n.xhrFields[u];
                    n.mimeType && a.overrideMimeType && a.overrideMimeType(n.mimeType);
                    !n.crossDomain && !i["X-Requested-With"] && (i["X-Requested-With"] = "XMLHttpRequest");
                    try {
                        for (u in i) a.setRequestHeader(u, i[u]);
                    } catch (f) {}
                    a.send(n.hasContent && n.data || null);
                    r = function(e, i) {
                        var u, f, l, c;
                        try {
                            if (r && (i || a.readyState === 4)) {
                                r = t;
                                if (o) {
                                    a.onreadystatechange = w.noop;
                                    Un && delete In[o];
                                }
                                if (i) a.readyState !== 4 && a.abort(); else {
                                    c = {};
                                    u = a.status;
                                    f = a.getAllResponseHeaders();
                                    typeof a.responseText == "string" && (c.text = a.responseText);
                                    try {
                                        l = a.statusText;
                                    } catch (h) {
                                        l = "";
                                    }
                                    !u && n.isLocal && !n.crossDomain ? u = c.text ? 200 : 404 : u === 1223 && (u = 204);
                                }
                            }
                        } catch (p) {
                            i || s(-1, p);
                        }
                        c && s(u, l, c, f);
                    };
                    if (!n.async) r(); else if (a.readyState === 4) setTimeout(r); else {
                        o = ++Rn;
                        if (Un) {
                            if (!In) {
                                In = {};
                                w(e).unload(Un);
                            }
                            In[o] = r;
                        }
                        a.onreadystatechange = r;
                    }
                },
                abort: function() {
                    r && r(t, !0);
                }
            };
        }
    });
    var Xn, Vn, $n = /^(?:toggle|show|hide)$/, Jn = new RegExp("^(?:([+-])=|)(" + E + ")([a-z%]*)$", "i"), Kn = /queueHooks$/, Qn = [ nr ], Gn = {
        "*": [ function(e, t) {
            var n = this.createTween(e, t), r = n.cur(), i = Jn.exec(t), s = i && i[3] || (w.cssNumber[e] ? "" : "px"), o = (w.cssNumber[e] || s !== "px" && +r) && Jn.exec(w.css(n.elem, e)), u = 1, a = 20;
            if (o && o[3] !== s) {
                s = s || o[3];
                i = i || [];
                o = +r || 1;
                do {
                    u = u || ".5";
                    o /= u;
                    w.style(n.elem, e, o + s);
                } while (u !== (u = n.cur() / r) && u !== 1 && --a);
            }
            if (i) {
                o = n.start = +o || +r || 0;
                n.unit = s;
                n.end = i[1] ? o + (i[1] + 1) * i[2] : +i[2];
            }
            return n;
        } ]
    };
    w.Animation = w.extend(er, {
        tweener: function(e, t) {
            if (w.isFunction(e)) {
                t = e;
                e = [ "*" ];
            } else e = e.split(" ");
            var n, r = 0, i = e.length;
            for (; r < i; r++) {
                n = e[r];
                Gn[n] = Gn[n] || [];
                Gn[n].unshift(t);
            }
        },
        prefilter: function(e, t) {
            t ? Qn.unshift(e) : Qn.push(e);
        }
    });
    w.Tween = rr;
    rr.prototype = {
        constructor: rr,
        init: function(e, t, n, r, i, s) {
            this.elem = e;
            this.prop = n;
            this.easing = i || "swing";
            this.options = t;
            this.start = this.now = this.cur();
            this.end = r;
            this.unit = s || (w.cssNumber[n] ? "" : "px");
        },
        cur: function() {
            var e = rr.propHooks[this.prop];
            return e && e.get ? e.get(this) : rr.propHooks._default.get(this);
        },
        run: function(e) {
            var t, n = rr.propHooks[this.prop];
            this.options.duration ? this.pos = t = w.easing[this.easing](e, this.options.duration * e, 0, 1, this.options.duration) : this.pos = t = e;
            this.now = (this.end - this.start) * t + this.start;
            this.options.step && this.options.step.call(this.elem, this.now, this);
            n && n.set ? n.set(this) : rr.propHooks._default.set(this);
            return this;
        }
    };
    rr.prototype.init.prototype = rr.prototype;
    rr.propHooks = {
        _default: {
            get: function(e) {
                var t;
                if (e.elem[e.prop] == null || !!e.elem.style && e.elem.style[e.prop] != null) {
                    t = w.css(e.elem, e.prop, "");
                    return !t || t === "auto" ? 0 : t;
                }
                return e.elem[e.prop];
            },
            set: function(e) {
                w.fx.step[e.prop] ? w.fx.step[e.prop](e) : e.elem.style && (e.elem.style[w.cssProps[e.prop]] != null || w.cssHooks[e.prop]) ? w.style(e.elem, e.prop, e.now + e.unit) : e.elem[e.prop] = e.now;
            }
        }
    };
    rr.propHooks.scrollTop = rr.propHooks.scrollLeft = {
        set: function(e) {
            e.elem.nodeType && e.elem.parentNode && (e.elem[e.prop] = e.now);
        }
    };
    w.each([ "toggle", "show", "hide" ], function(e, t) {
        var n = w.fn[t];
        w.fn[t] = function(e, r, i) {
            return e == null || typeof e == "boolean" ? n.apply(this, arguments) : this.animate(ir(t, !0), e, r, i);
        };
    });
    w.fn.extend({
        fadeTo: function(e, t, n, r) {
            return this.filter(nn).css("opacity", 0).show().end().animate({
                opacity: t
            }, e, n, r);
        },
        animate: function(e, t, n, r) {
            var i = w.isEmptyObject(e), s = w.speed(t, n, r), o = function() {
                var t = er(this, w.extend({}, e), s);
                (i || w._data(this, "finish")) && t.stop(!0);
            };
            o.finish = o;
            return i || s.queue === !1 ? this.each(o) : this.queue(s.queue, o);
        },
        stop: function(e, n, r) {
            var i = function(e) {
                var t = e.stop;
                delete e.stop;
                t(r);
            };
            if (typeof e != "string") {
                r = n;
                n = e;
                e = t;
            }
            n && e !== !1 && this.queue(e || "fx", []);
            return this.each(function() {
                var t = !0, n = e != null && e + "queueHooks", s = w.timers, o = w._data(this);
                if (n) o[n] && o[n].stop && i(o[n]); else for (n in o) o[n] && o[n].stop && Kn.test(n) && i(o[n]);
                for (n = s.length; n--; ) if (s[n].elem === this && (e == null || s[n].queue === e)) {
                    s[n].anim.stop(r);
                    t = !1;
                    s.splice(n, 1);
                }
                (t || !r) && w.dequeue(this, e);
            });
        },
        finish: function(e) {
            e !== !1 && (e = e || "fx");
            return this.each(function() {
                var t, n = w._data(this), r = n[e + "queue"], i = n[e + "queueHooks"], s = w.timers, o = r ? r.length : 0;
                n.finish = !0;
                w.queue(this, e, []);
                i && i.stop && i.stop.call(this, !0);
                for (t = s.length; t--; ) if (s[t].elem === this && s[t].queue === e) {
                    s[t].anim.stop(!0);
                    s.splice(t, 1);
                }
                for (t = 0; t < o; t++) r[t] && r[t].finish && r[t].finish.call(this);
                delete n.finish;
            });
        }
    });
    w.each({
        slideDown: ir("show"),
        slideUp: ir("hide"),
        slideToggle: ir("toggle"),
        fadeIn: {
            opacity: "show"
        },
        fadeOut: {
            opacity: "hide"
        },
        fadeToggle: {
            opacity: "toggle"
        }
    }, function(e, t) {
        w.fn[e] = function(e, n, r) {
            return this.animate(t, e, n, r);
        };
    });
    w.speed = function(e, t, n) {
        var r = e && typeof e == "object" ? w.extend({}, e) : {
            complete: n || !n && t || w.isFunction(e) && e,
            duration: e,
            easing: n && t || t && !w.isFunction(t) && t
        };
        r.duration = w.fx.off ? 0 : typeof r.duration == "number" ? r.duration : r.duration in w.fx.speeds ? w.fx.speeds[r.duration] : w.fx.speeds._default;
        if (r.queue == null || r.queue === !0) r.queue = "fx";
        r.old = r.complete;
        r.complete = function() {
            w.isFunction(r.old) && r.old.call(this);
            r.queue && w.dequeue(this, r.queue);
        };
        return r;
    };
    w.easing = {
        linear: function(e) {
            return e;
        },
        swing: function(e) {
            return .5 - Math.cos(e * Math.PI) / 2;
        }
    };
    w.timers = [];
    w.fx = rr.prototype.init;
    w.fx.tick = function() {
        var e, n = w.timers, r = 0;
        Xn = w.now();
        for (; r < n.length; r++) {
            e = n[r];
            !e() && n[r] === e && n.splice(r--, 1);
        }
        n.length || w.fx.stop();
        Xn = t;
    };
    w.fx.timer = function(e) {
        e() && w.timers.push(e) && w.fx.start();
    };
    w.fx.interval = 13;
    w.fx.start = function() {
        Vn || (Vn = setInterval(w.fx.tick, w.fx.interval));
    };
    w.fx.stop = function() {
        clearInterval(Vn);
        Vn = null;
    };
    w.fx.speeds = {
        slow: 600,
        fast: 200,
        _default: 400
    };
    w.fx.step = {};
    w.expr && w.expr.filters && (w.expr.filters.animated = function(e) {
        return w.grep(w.timers, function(t) {
            return e === t.elem;
        }).length;
    });
    w.fn.offset = function(e) {
        if (arguments.length) return e === t ? this : this.each(function(t) {
            w.offset.setOffset(this, e, t);
        });
        var n, r, s = {
            top: 0,
            left: 0
        }, o = this[0], u = o && o.ownerDocument;
        if (!u) return;
        n = u.documentElement;
        if (!w.contains(n, o)) return s;
        typeof o.getBoundingClientRect !== i && (s = o.getBoundingClientRect());
        r = sr(u);
        return {
            top: s.top + (r.pageYOffset || n.scrollTop) - (n.clientTop || 0),
            left: s.left + (r.pageXOffset || n.scrollLeft) - (n.clientLeft || 0)
        };
    };
    w.offset = {
        setOffset: function(e, t, n) {
            var r = w.css(e, "position");
            r === "static" && (e.style.position = "relative");
            var i = w(e), s = i.offset(), o = w.css(e, "top"), u = w.css(e, "left"), a = (r === "absolute" || r === "fixed") && w.inArray("auto", [ o, u ]) > -1, f = {}, l = {}, c, h;
            if (a) {
                l = i.position();
                c = l.top;
                h = l.left;
            } else {
                c = parseFloat(o) || 0;
                h = parseFloat(u) || 0;
            }
            w.isFunction(t) && (t = t.call(e, n, s));
            t.top != null && (f.top = t.top - s.top + c);
            t.left != null && (f.left = t.left - s.left + h);
            "using" in t ? t.using.call(e, f) : i.css(f);
        }
    };
    w.fn.extend({
        position: function() {
            if (!this[0]) return;
            var e, t, n = {
                top: 0,
                left: 0
            }, r = this[0];
            if (w.css(r, "position") === "fixed") t = r.getBoundingClientRect(); else {
                e = this.offsetParent();
                t = this.offset();
                w.nodeName(e[0], "html") || (n = e.offset());
                n.top += w.css(e[0], "borderTopWidth", !0);
                n.left += w.css(e[0], "borderLeftWidth", !0);
            }
            return {
                top: t.top - n.top - w.css(r, "marginTop", !0),
                left: t.left - n.left - w.css(r, "marginLeft", !0)
            };
        },
        offsetParent: function() {
            return this.map(function() {
                var e = this.offsetParent || u;
                while (e && !w.nodeName(e, "html") && w.css(e, "position") === "static") e = e.offsetParent;
                return e || u;
            });
        }
    });
    w.each({
        scrollLeft: "pageXOffset",
        scrollTop: "pageYOffset"
    }, function(e, n) {
        var r = /Y/.test(n);
        w.fn[e] = function(i) {
            return w.access(this, function(e, i, s) {
                var o = sr(e);
                if (s === t) return o ? n in o ? o[n] : o.document.documentElement[i] : e[i];
                o ? o.scrollTo(r ? w(o).scrollLeft() : s, r ? s : w(o).scrollTop()) : e[i] = s;
            }, e, i, arguments.length, null);
        };
    });
    w.each({
        Height: "height",
        Width: "width"
    }, function(e, n) {
        w.each({
            padding: "inner" + e,
            content: n,
            "": "outer" + e
        }, function(r, i) {
            w.fn[i] = function(i, s) {
                var o = arguments.length && (r || typeof i != "boolean"), u = r || (i === !0 || s === !0 ? "margin" : "border");
                return w.access(this, function(n, r, i) {
                    var s;
                    if (w.isWindow(n)) return n.document.documentElement["client" + e];
                    if (n.nodeType === 9) {
                        s = n.documentElement;
                        return Math.max(n.body["scroll" + e], s["scroll" + e], n.body["offset" + e], s["offset" + e], s["client" + e]);
                    }
                    return i === t ? w.css(n, r, u) : w.style(n, r, i, u);
                }, n, o ? i : t, o, null);
            };
        });
    });
    w.fn.size = function() {
        return this.length;
    };
    w.fn.andSelf = w.fn.addBack;
    if (typeof module == "object" && module && typeof module.exports == "object") module.exports = w; else {
        e.jQuery = e.$ = w;
        typeof define == "function" && define.amd && define("jquery", [], function() {
            return w;
        });
    }
})(window);

!function(e) {
    var t = '[data-dismiss="alert"]', n = function(n) {
        e(n).on("click", t, this.close);
    };
    n.prototype.close = function(t) {
        function s() {
            i.trigger("closed").remove();
        }
        var n = e(this), r = n.attr("data-target"), i;
        if (!r) {
            r = n.attr("href");
            r = r && r.replace(/.*(?=#[^\s]*$)/, "");
        }
        i = e(r);
        t && t.preventDefault();
        i.length || (i = n.hasClass("alert") ? n : n.parent());
        i.trigger(t = e.Event("close"));
        if (t.isDefaultPrevented()) return;
        i.removeClass("in");
        e.support.transition && i.hasClass("fade") ? i.on(e.support.transition.end, s) : s();
    };
    var r = e.fn.alert;
    e.fn.alert = function(t) {
        return this.each(function() {
            var r = e(this), i = r.data("alert");
            i || r.data("alert", i = new n(this));
            typeof t == "string" && i[t].call(r);
        });
    };
    e.fn.alert.Constructor = n;
    e.fn.alert.noConflict = function() {
        e.fn.alert = r;
        return this;
    };
    e(document).on("click.alert.data-api", t, n.prototype.close);
}(window.jQuery);

!function(e) {
    e(function() {
        e.support.transition = function() {
            var e = function() {
                var e = document.createElement("bootstrap"), t = {
                    WebkitTransition: "webkitTransitionEnd",
                    MozTransition: "transitionend",
                    OTransition: "oTransitionEnd otransitionend",
                    transition: "transitionend"
                }, n;
                for (n in t) if (e.style[n] !== undefined) return t[n];
            }();
            return e && {
                end: e
            };
        }();
    });
}(window.jQuery);

!function(e) {
    var t = function(t, n) {
        this.$element = e(t);
        this.options = e.extend({}, e.fn.collapse.defaults, n);
        this.options.parent && (this.$parent = e(this.options.parent));
        this.options.toggle && this.toggle();
    };
    t.prototype = {
        constructor: t,
        dimension: function() {
            var e = this.$element.hasClass("width");
            return e ? "width" : "height";
        },
        show: function() {
            var t, n, r, i;
            if (this.transitioning || this.$element.hasClass("in")) return;
            t = this.dimension();
            n = e.camelCase([ "scroll", t ].join("-"));
            r = this.$parent && this.$parent.find("> .accordion-group > .in");
            if (r && r.length) {
                i = r.data("collapse");
                if (i && i.transitioning) return;
                r.collapse("hide");
                i || r.data("collapse", null);
            }
            this.$element[t](0);
            this.transition("addClass", e.Event("show"), "shown");
            e.support.transition && this.$element[t](this.$element[0][n]);
        },
        hide: function() {
            var t;
            if (this.transitioning || !this.$element.hasClass("in")) return;
            t = this.dimension();
            this.reset(this.$element[t]());
            this.transition("removeClass", e.Event("hide"), "hidden");
            this.$element[t](0);
        },
        reset: function(e) {
            var t = this.dimension();
            this.$element.removeClass("collapse")[t](e || "auto")[0].offsetWidth;
            this.$element[e !== null ? "addClass" : "removeClass"]("collapse");
            return this;
        },
        transition: function(t, n, r) {
            var i = this, s = function() {
                n.type == "show" && i.reset();
                i.transitioning = 0;
                i.$element.trigger(r);
            };
            this.$element.trigger(n);
            if (n.isDefaultPrevented()) return;
            this.transitioning = 1;
            this.$element[t]("in");
            e.support.transition && this.$element.hasClass("collapse") ? this.$element.one(e.support.transition.end, s) : s();
        },
        toggle: function() {
            this[this.$element.hasClass("in") ? "hide" : "show"]();
        }
    };
    var n = e.fn.collapse;
    e.fn.collapse = function(n) {
        return this.each(function() {
            var r = e(this), i = r.data("collapse"), s = e.extend({}, e.fn.collapse.defaults, r.data(), typeof n == "object" && n);
            i || r.data("collapse", i = new t(this, s));
            typeof n == "string" && i[n]();
        });
    };
    e.fn.collapse.defaults = {
        toggle: !0
    };
    e.fn.collapse.Constructor = t;
    e.fn.collapse.noConflict = function() {
        e.fn.collapse = n;
        return this;
    };
    e(document).on("click.collapse.data-api", "[data-toggle=collapse]", function(t) {
        var n = e(this), r, i = n.attr("data-target") || t.preventDefault() || (r = n.attr("href")) && r.replace(/.*(?=#[^\s]+$)/, ""), s = e(i).data("collapse") ? "toggle" : n.data();
        n[e(i).hasClass("in") ? "addClass" : "removeClass"]("collapsed");
        e(i).collapse(s);
    });
}(window.jQuery);

!function(e) {
    var t = function(t, n) {
        this.$element = e(t);
        this.options = e.extend({}, e.fn.button.defaults, n);
    };
    t.prototype.setState = function(e) {
        var t = "disabled", n = this.$element, r = n.data(), i = n.is("input") ? "val" : "html";
        e += "Text";
        r.resetText || n.data("resetText", n[i]());
        n[i](r[e] || this.options[e]);
        setTimeout(function() {
            e == "loadingText" ? n.addClass(t).attr(t, t) : n.removeClass(t).removeAttr(t);
        }, 0);
    };
    t.prototype.toggle = function() {
        var e = this.$element.closest('[data-toggle="buttons-radio"]');
        e && e.find(".active").removeClass("active");
        this.$element.toggleClass("active");
    };
    var n = e.fn.button;
    e.fn.button = function(n) {
        return this.each(function() {
            var r = e(this), i = r.data("button"), s = typeof n == "object" && n;
            i || r.data("button", i = new t(this, s));
            n == "toggle" ? i.toggle() : n && i.setState(n);
        });
    };
    e.fn.button.defaults = {
        loadingText: "loading..."
    };
    e.fn.button.Constructor = t;
    e.fn.button.noConflict = function() {
        e.fn.button = n;
        return this;
    };
    e(document).on("click.button.data-api", "[data-toggle^=button]", function(t) {
        var n = e(t.target);
        n.hasClass("btn") || (n = n.closest(".btn"));
        n.button("toggle");
    });
}(window.jQuery);

!function(e) {
    function r() {
        e(t).each(function() {
            i(e(this)).removeClass("open");
        });
    }
    function i(t) {
        var n = t.attr("data-target"), r;
        if (!n) {
            n = t.attr("href");
            n = n && /#/.test(n) && n.replace(/.*(?=#[^\s]*$)/, "");
        }
        r = n && e(n);
        if (!r || !r.length) r = t.parent();
        return r;
    }
    var t = "[data-toggle=dropdown]", n = function(t) {
        var n = e(t).on("click.dropdown.data-api", this.toggle);
        e("html").on("click.dropdown.data-api", function() {
            n.parent().removeClass("open");
        });
    };
    n.prototype = {
        constructor: n,
        toggle: function(t) {
            var n = e(this), s, o;
            if (n.is(".disabled, :disabled")) return;
            s = i(n);
            o = s.hasClass("open");
            r();
            o || s.toggleClass("open");
            n.focus();
            return !1;
        },
        keydown: function(n) {
            var r, s, o, u, a, f;
            if (!/(38|40|27)/.test(n.keyCode)) return;
            r = e(this);
            n.preventDefault();
            n.stopPropagation();
            if (r.is(".disabled, :disabled")) return;
            u = i(r);
            a = u.hasClass("open");
            if (!a || a && n.keyCode == 27) {
                n.which == 27 && u.find(t).focus();
                return r.click();
            }
            s = e("[role=menu] li:not(.divider):visible a", u);
            if (!s.length) return;
            f = s.index(s.filter(":focus"));
            n.keyCode == 38 && f > 0 && f--;
            n.keyCode == 40 && f < s.length - 1 && f++;
            ~f || (f = 0);
            s.eq(f).focus();
        }
    };
    var s = e.fn.dropdown;
    e.fn.dropdown = function(t) {
        return this.each(function() {
            var r = e(this), i = r.data("dropdown");
            i || r.data("dropdown", i = new n(this));
            typeof t == "string" && i[t].call(r);
        });
    };
    e.fn.dropdown.Constructor = n;
    e.fn.dropdown.noConflict = function() {
        e.fn.dropdown = s;
        return this;
    };
    e(document).on("click.dropdown.data-api", r).on("click.dropdown.data-api", ".dropdown form", function(e) {
        e.stopPropagation();
    }).on("click.dropdown-menu", function(e) {
        e.stopPropagation();
    }).on("click.dropdown.data-api", t, n.prototype.toggle).on("keydown.dropdown.data-api", t + ", [role=menu]", n.prototype.keydown);
}(window.jQuery);

!function(e) {
    var t = function(t, n) {
        this.$element = e(t);
        this.options = e.extend({}, e.fn.typeahead.defaults, n);
        this.matcher = this.options.matcher || this.matcher;
        this.sorter = this.options.sorter || this.sorter;
        this.highlighter = this.options.highlighter || this.highlighter;
        this.updater = this.options.updater || this.updater;
        this.source = this.options.source;
        this.$menu = e(this.options.menu);
        this.shown = !1;
        this.listen();
    };
    t.prototype = {
        constructor: t,
        select: function() {
            var e = this.$menu.find(".active").attr("data-value");
            this.$element.val(this.updater(e)).change();
            return this.hide();
        },
        updater: function(e) {
            return e;
        },
        show: function() {
            var t = e.extend({}, this.$element.position(), {
                height: this.$element[0].offsetHeight
            });
            this.$menu.insertAfter(this.$element).css({
                top: t.top + t.height,
                left: t.left
            }).show();
            this.shown = !0;
            return this;
        },
        hide: function() {
            this.$menu.hide();
            this.shown = !1;
            return this;
        },
        lookup: function(t) {
            var n;
            this.query = this.$element.val();
            if (!this.query || this.query.length < this.options.minLength) return this.shown ? this.hide() : this;
            n = e.isFunction(this.source) ? this.source(this.query, e.proxy(this.process, this)) : this.source;
            return n ? this.process(n) : this;
        },
        process: function(t) {
            var n = this;
            t = e.grep(t, function(e) {
                return n.matcher(e);
            });
            t = this.sorter(t);
            return t.length ? this.render(t.slice(0, this.options.items)).show() : this.shown ? this.hide() : this;
        },
        matcher: function(e) {
            return ~e.toLowerCase().indexOf(this.query.toLowerCase());
        },
        sorter: function(e) {
            var t = [], n = [], r = [], i;
            while (i = e.shift()) i.toLowerCase().indexOf(this.query.toLowerCase()) ? ~i.indexOf(this.query) ? n.push(i) : r.push(i) : t.push(i);
            return t.concat(n, r);
        },
        highlighter: function(e) {
            var t = this.query.replace(/[\-\[\]{}()*+?.,\\\^$|#\s]/g, "\\$&");
            return e.replace(new RegExp("(" + t + ")", "ig"), function(e, t) {
                return "<strong>" + t + "</strong>";
            });
        },
        render: function(t) {
            var n = this;
            t = e(t).map(function(t, r) {
                t = e(n.options.item).attr("data-value", r);
                t.find("a").html(n.highlighter(r));
                return t[0];
            });
            t.first().addClass("active");
            this.$menu.html(t);
            return this;
        },
        next: function(t) {
            var n = this.$menu.find(".active").removeClass("active"), r = n.next();
            r.length || (r = e(this.$menu.find("li")[0]));
            r.addClass("active");
        },
        prev: function(e) {
            var t = this.$menu.find(".active").removeClass("active"), n = t.prev();
            n.length || (n = this.$menu.find("li").last());
            n.addClass("active");
        },
        listen: function() {
            this.$element.on("focus", e.proxy(this.focus, this)).on("blur", e.proxy(this.blur, this)).on("keypress", e.proxy(this.keypress, this)).on("keyup", e.proxy(this.keyup, this));
            this.eventSupported("keydown") && this.$element.on("keydown", e.proxy(this.keydown, this));
            this.$menu.on("click", e.proxy(this.click, this)).on("mouseenter", "li", e.proxy(this.mouseenter, this)).on("mouseleave", "li", e.proxy(this.mouseleave, this));
        },
        eventSupported: function(e) {
            var t = e in this.$element;
            if (!t) {
                this.$element.setAttribute(e, "return;");
                t = typeof this.$element[e] == "function";
            }
            return t;
        },
        move: function(e) {
            if (!this.shown) return;
            switch (e.keyCode) {
              case 9:
              case 13:
              case 27:
                e.preventDefault();
                break;
              case 38:
                e.preventDefault();
                this.prev();
                break;
              case 40:
                e.preventDefault();
                this.next();
            }
            e.stopPropagation();
        },
        keydown: function(t) {
            this.suppressKeyPressRepeat = ~e.inArray(t.keyCode, [ 40, 38, 9, 13, 27 ]);
            this.move(t);
        },
        keypress: function(e) {
            if (this.suppressKeyPressRepeat) return;
            this.move(e);
        },
        keyup: function(e) {
            switch (e.keyCode) {
              case 40:
              case 38:
              case 16:
              case 17:
              case 18:
                break;
              case 9:
              case 13:
                if (!this.shown) return;
                this.select();
                break;
              case 27:
                if (!this.shown) return;
                this.hide();
                break;
              default:
                this.lookup();
            }
            e.stopPropagation();
            e.preventDefault();
        },
        focus: function(e) {
            this.focused = !0;
        },
        blur: function(e) {
            this.focused = !1;
            !this.mousedover && this.shown && this.hide();
        },
        click: function(e) {
            e.stopPropagation();
            e.preventDefault();
            this.select();
            this.$element.focus();
        },
        mouseenter: function(t) {
            this.mousedover = !0;
            this.$menu.find(".active").removeClass("active");
            e(t.currentTarget).addClass("active");
        },
        mouseleave: function(e) {
            this.mousedover = !1;
            !this.focused && this.shown && this.hide();
        }
    };
    var n = e.fn.typeahead;
    e.fn.typeahead = function(n) {
        return this.each(function() {
            var r = e(this), i = r.data("typeahead"), s = typeof n == "object" && n;
            i || r.data("typeahead", i = new t(this, s));
            typeof n == "string" && i[n]();
        });
    };
    e.fn.typeahead.defaults = {
        source: [],
        items: 8,
        menu: '<ul class="typeahead dropdown-menu"></ul>',
        item: '<li><a href="#"></a></li>',
        minLength: 1
    };
    e.fn.typeahead.Constructor = t;
    e.fn.typeahead.noConflict = function() {
        e.fn.typeahead = n;
        return this;
    };
    e(document).on("focus.typeahead.data-api", '[data-provide="typeahead"]', function(t) {
        var n = e(this);
        if (n.data("typeahead")) return;
        n.typeahead(n.data());
    });
}(window.jQuery);

!function(e) {
    var t = function(t, n) {
        this.$element = e(t);
        this.$indicators = this.$element.find(".carousel-indicators");
        this.options = n;
        this.options.pause == "hover" && this.$element.on("mouseenter", e.proxy(this.pause, this)).on("mouseleave", e.proxy(this.cycle, this));
    };
    t.prototype = {
        cycle: function(t) {
            t || (this.paused = !1);
            this.interval && clearInterval(this.interval);
            this.options.interval && !this.paused && (this.interval = setInterval(e.proxy(this.next, this), this.options.interval));
            return this;
        },
        getActiveIndex: function() {
            this.$active = this.$element.find(".item.active");
            this.$items = this.$active.parent().children();
            return this.$items.index(this.$active);
        },
        to: function(t) {
            var n = this.getActiveIndex(), r = this;
            if (t > this.$items.length - 1 || t < 0) return;
            return this.sliding ? this.$element.one("slid", function() {
                r.to(t);
            }) : n == t ? this.pause().cycle() : this.slide(t > n ? "next" : "prev", e(this.$items[t]));
        },
        pause: function(t) {
            t || (this.paused = !0);
            if (this.$element.find(".next, .prev").length && e.support.transition.end) {
                this.$element.trigger(e.support.transition.end);
                this.cycle(!0);
            }
            clearInterval(this.interval);
            this.interval = null;
            return this;
        },
        next: function() {
            if (this.sliding) return;
            return this.slide("next");
        },
        prev: function() {
            if (this.sliding) return;
            return this.slide("prev");
        },
        slide: function(t, n) {
            var r = this.$element.find(".item.active"), i = n || r[t](), s = this.interval, o = t == "next" ? "left" : "right", u = t == "next" ? "first" : "last", a = this, f;
            this.sliding = !0;
            s && this.pause();
            i = i.length ? i : this.$element.find(".item")[u]();
            f = e.Event("slide", {
                relatedTarget: i[0],
                direction: o
            });
            if (i.hasClass("active")) return;
            if (this.$indicators.length) {
                this.$indicators.find(".active").removeClass("active");
                this.$element.one("slid", function() {
                    var t = e(a.$indicators.children()[a.getActiveIndex()]);
                    t && t.addClass("active");
                });
            }
            if (e.support.transition && this.$element.hasClass("slide")) {
                this.$element.trigger(f);
                if (f.isDefaultPrevented()) return;
                i.addClass(t);
                i[0].offsetWidth;
                r.addClass(o);
                i.addClass(o);
                this.$element.one(e.support.transition.end, function() {
                    i.removeClass([ t, o ].join(" ")).addClass("active");
                    r.removeClass([ "active", o ].join(" "));
                    a.sliding = !1;
                    setTimeout(function() {
                        a.$element.trigger("slid");
                    }, 0);
                });
            } else {
                this.$element.trigger(f);
                if (f.isDefaultPrevented()) return;
                r.removeClass("active");
                i.addClass("active");
                this.sliding = !1;
                this.$element.trigger("slid");
            }
            s && this.cycle();
            return this;
        }
    };
    var n = e.fn.carousel;
    e.fn.carousel = function(n) {
        return this.each(function() {
            var r = e(this), i = r.data("carousel"), s = e.extend({}, e.fn.carousel.defaults, typeof n == "object" && n), o = typeof n == "string" ? n : s.slide;
            i || r.data("carousel", i = new t(this, s));
            typeof n == "number" ? i.to(n) : o ? i[o]() : s.interval && i.pause().cycle();
        });
    };
    e.fn.carousel.defaults = {
        interval: 5e3,
        pause: "hover"
    };
    e.fn.carousel.Constructor = t;
    e.fn.carousel.noConflict = function() {
        e.fn.carousel = n;
        return this;
    };
    e(document).on("click.carousel.data-api", "[data-slide], [data-slide-to]", function(t) {
        var n = e(this), r, i = e(n.attr("data-target") || (r = n.attr("href")) && r.replace(/.*(?=#[^\s]+$)/, "")), s = e.extend({}, i.data(), n.data()), o;
        i.carousel(s);
        (o = n.attr("data-slide-to")) && i.data("carousel").pause().to(o).cycle();
        t.preventDefault();
    });
}(window.jQuery);

!function(e) {
    var t = function(t, n) {
        this.options = n;
        this.$element = e(t).delegate('[data-dismiss="modal"]', "click.dismiss.modal", e.proxy(this.hide, this));
        this.options.remote && this.$element.find(".modal-body").load(this.options.remote);
    };
    t.prototype = {
        constructor: t,
        toggle: function() {
            return this[this.isShown ? "hide" : "show"]();
        },
        show: function() {
            var t = this, n = e.Event("show");
            this.$element.trigger(n);
            if (this.isShown || n.isDefaultPrevented()) return;
            this.isShown = !0;
            this.escape();
            this.backdrop(function() {
                var n = e.support.transition && t.$element.hasClass("fade");
                t.$element.parent().length || t.$element.appendTo(document.body);
                t.$element.show();
                n && t.$element[0].offsetWidth;
                t.$element.addClass("in").attr("aria-hidden", !1);
                t.enforceFocus();
                n ? t.$element.one(e.support.transition.end, function() {
                    t.$element.focus().trigger("shown");
                }) : t.$element.focus().trigger("shown");
            });
        },
        hide: function(t) {
            t && t.preventDefault();
            var n = this;
            t = e.Event("hide");
            this.$element.trigger(t);
            if (!this.isShown || t.isDefaultPrevented()) return;
            this.isShown = !1;
            this.escape();
            e(document).off("focusin.modal");
            this.$element.removeClass("in").attr("aria-hidden", !0);
            e.support.transition && this.$element.hasClass("fade") ? this.hideWithTransition() : this.hideModal();
        },
        enforceFocus: function() {
            var t = this;
            e(document).on("focusin.modal", function(e) {
                t.$element[0] !== e.target && !t.$element.has(e.target).length && t.$element.focus();
            });
        },
        escape: function() {
            var e = this;
            this.isShown && this.options.keyboard ? this.$element.on("keyup.dismiss.modal", function(t) {
                t.which == 27 && e.hide();
            }) : this.isShown || this.$element.off("keyup.dismiss.modal");
        },
        hideWithTransition: function() {
            var t = this, n = setTimeout(function() {
                t.$element.off(e.support.transition.end);
                t.hideModal();
            }, 500);
            this.$element.one(e.support.transition.end, function() {
                clearTimeout(n);
                t.hideModal();
            });
        },
        hideModal: function() {
            var e = this;
            this.$element.hide();
            this.backdrop(function() {
                e.removeBackdrop();
                e.$element.trigger("hidden");
            });
        },
        removeBackdrop: function() {
            this.$backdrop && this.$backdrop.remove();
            this.$backdrop = null;
        },
        backdrop: function(t) {
            var n = this, r = this.$element.hasClass("fade") ? "fade" : "";
            if (this.isShown && this.options.backdrop) {
                var i = e.support.transition && r;
                this.$backdrop = e('<div class="modal-backdrop ' + r + '" />').appendTo(document.body);
                this.$backdrop.click(this.options.backdrop == "static" ? e.proxy(this.$element[0].focus, this.$element[0]) : e.proxy(this.hide, this));
                i && this.$backdrop[0].offsetWidth;
                this.$backdrop.addClass("in");
                if (!t) return;
                i ? this.$backdrop.one(e.support.transition.end, t) : t();
            } else if (!this.isShown && this.$backdrop) {
                this.$backdrop.removeClass("in");
                e.support.transition && this.$element.hasClass("fade") ? this.$backdrop.one(e.support.transition.end, t) : t();
            } else t && t();
        }
    };
    var n = e.fn.modal;
    e.fn.modal = function(n) {
        return this.each(function() {
            var r = e(this), i = r.data("modal"), s = e.extend({}, e.fn.modal.defaults, r.data(), typeof n == "object" && n);
            i || r.data("modal", i = new t(this, s));
            typeof n == "string" ? i[n]() : s.show && i.show();
        });
    };
    e.fn.modal.defaults = {
        backdrop: !0,
        keyboard: !0,
        show: !0
    };
    e.fn.modal.Constructor = t;
    e.fn.modal.noConflict = function() {
        e.fn.modal = n;
        return this;
    };
    e(document).on("click.modal.data-api", '[data-toggle="modal"]', function(t) {
        var n = e(this), r = n.attr("href"), i = e(n.attr("data-target") || r && r.replace(/.*(?=#[^\s]+$)/, "")), s = i.data("modal") ? "toggle" : e.extend({
            remote: !/#/.test(r) && r
        }, i.data(), n.data());
        t.preventDefault();
        i.modal(s).one("hide", function() {
            n.focus();
        });
    });
}(window.jQuery);

!function(e) {
    var t = function(t, n) {
        this.options = e.extend({}, e.fn.affix.defaults, n);
        this.$window = e(window).on("scroll.affix.data-api", e.proxy(this.checkPosition, this)).on("click.affix.data-api", e.proxy(function() {
            setTimeout(e.proxy(this.checkPosition, this), 1);
        }, this));
        this.$element = e(t);
        this.checkPosition();
    };
    t.prototype.checkPosition = function() {
        if (!this.$element.is(":visible")) return;
        var t = e(document).height(), n = this.$window.scrollTop(), r = this.$element.offset(), i = this.options.offset, s = i.bottom, o = i.top, u = "affix affix-top affix-bottom", a;
        typeof i != "object" && (s = o = i);
        typeof o == "function" && (o = i.top());
        typeof s == "function" && (s = i.bottom());
        a = this.unpin != null && n + this.unpin <= r.top ? !1 : s != null && r.top + this.$element.height() >= t - s ? "bottom" : o != null && n <= o ? "top" : !1;
        if (this.affixed === a) return;
        this.affixed = a;
        this.unpin = a == "bottom" ? r.top - n : null;
        this.$element.removeClass(u).addClass("affix" + (a ? "-" + a : ""));
    };
    var n = e.fn.affix;
    e.fn.affix = function(n) {
        return this.each(function() {
            var r = e(this), i = r.data("affix"), s = typeof n == "object" && n;
            i || r.data("affix", i = new t(this, s));
            typeof n == "string" && i[n]();
        });
    };
    e.fn.affix.Constructor = t;
    e.fn.affix.defaults = {
        offset: 0
    };
    e.fn.affix.noConflict = function() {
        e.fn.affix = n;
        return this;
    };
    e(window).on("load", function() {
        e('[data-spy="affix"]').each(function() {
            var t = e(this), n = t.data();
            n.offset = n.offset || {};
            n.offsetBottom && (n.offset.bottom = n.offsetBottom);
            n.offsetTop && (n.offset.top = n.offsetTop);
            t.affix(n);
        });
    });
}(window.jQuery);

!function(e) {
    function t(t, n) {
        var r = e.proxy(this.process, this), i = e(t).is("body") ? e(window) : e(t), s;
        this.options = e.extend({}, e.fn.scrollspy.defaults, n);
        this.$scrollElement = i.on("scroll.scroll-spy.data-api", r);
        this.selector = (this.options.target || (s = e(t).attr("href")) && s.replace(/.*(?=#[^\s]+$)/, "") || "") + " .nav li > a";
        this.$body = e("body");
        this.refresh();
        this.process();
    }
    t.prototype = {
        constructor: t,
        refresh: function() {
            var t = this, n;
            this.offsets = e([]);
            this.targets = e([]);
            n = this.$body.find(this.selector).map(function() {
                var n = e(this), r = n.data("target") || n.attr("href"), i = /^#\w/.test(r) && e(r);
                return i && i.length && [ [ i.position().top + (!e.isWindow(t.$scrollElement.get(0)) && t.$scrollElement.scrollTop()), r ] ] || null;
            }).sort(function(e, t) {
                return e[0] - t[0];
            }).each(function() {
                t.offsets.push(this[0]);
                t.targets.push(this[1]);
            });
        },
        process: function() {
            var e = this.$scrollElement.scrollTop() + this.options.offset, t = this.$scrollElement[0].scrollHeight || this.$body[0].scrollHeight, n = t - this.$scrollElement.height(), r = this.offsets, i = this.targets, s = this.activeTarget, o;
            if (e >= n) return s != (o = i.last()[0]) && this.activate(o);
            for (o = r.length; o--; ) s != i[o] && e >= r[o] && (!r[o + 1] || e <= r[o + 1]) && this.activate(i[o]);
        },
        activate: function(t) {
            var n, r;
            this.activeTarget = t;
            e(this.selector).parent(".active").removeClass("active");
            r = this.selector + '[data-target="' + t + '"],' + this.selector + '[href="' + t + '"]';
            n = e(r).parent("li").addClass("active");
            n.parent(".dropdown-menu").length && (n = n.closest("li.dropdown").addClass("active"));
            n.trigger("activate");
        }
    };
    var n = e.fn.scrollspy;
    e.fn.scrollspy = function(n) {
        return this.each(function() {
            var r = e(this), i = r.data("scrollspy"), s = typeof n == "object" && n;
            i || r.data("scrollspy", i = new t(this, s));
            typeof n == "string" && i[n]();
        });
    };
    e.fn.scrollspy.Constructor = t;
    e.fn.scrollspy.defaults = {
        offset: 10
    };
    e.fn.scrollspy.noConflict = function() {
        e.fn.scrollspy = n;
        return this;
    };
    e(window).on("load", function() {
        e('[data-spy="scroll"]').each(function() {
            var t = e(this);
            t.scrollspy(t.data());
        });
    });
}(window.jQuery);

!function(e) {
    var t = function(t) {
        this.element = e(t);
    };
    t.prototype = {
        constructor: t,
        show: function() {
            var t = this.element, n = t.closest("ul:not(.dropdown-menu)"), r = t.attr("data-target"), i, s, o;
            if (!r) {
                r = t.attr("href");
                r = r && r.replace(/.*(?=#[^\s]*$)/, "");
            }
            if (t.parent("li").hasClass("active")) return;
            i = n.find(".active:last a")[0];
            o = e.Event("show", {
                relatedTarget: i
            });
            t.trigger(o);
            if (o.isDefaultPrevented()) return;
            s = e(r);
            this.activate(t.parent("li"), n);
            this.activate(s, s.parent(), function() {
                t.trigger({
                    type: "shown",
                    relatedTarget: i
                });
            });
        },
        activate: function(t, n, r) {
            function o() {
                i.removeClass("active").find("> .dropdown-menu > .active").removeClass("active");
                t.addClass("active");
                if (s) {
                    t[0].offsetWidth;
                    t.addClass("in");
                } else t.removeClass("fade");
                t.parent(".dropdown-menu") && t.closest("li.dropdown").addClass("active");
                r && r();
            }
            var i = n.find("> .active"), s = r && e.support.transition && i.hasClass("fade");
            s ? i.one(e.support.transition.end, o) : o();
            i.removeClass("in");
        }
    };
    var n = e.fn.tab;
    e.fn.tab = function(n) {
        return this.each(function() {
            var r = e(this), i = r.data("tab");
            i || r.data("tab", i = new t(this));
            typeof n == "string" && i[n]();
        });
    };
    e.fn.tab.Constructor = t;
    e.fn.tab.noConflict = function() {
        e.fn.tab = n;
        return this;
    };
    e(document).on("click.tab.data-api", '[data-toggle="tab"], [data-toggle="pill"]', function(t) {
        t.preventDefault();
        e(this).tab("show");
    });
}(window.jQuery);

!function(e) {
    var t = function(e, t) {
        this.init("tooltip", e, t);
    };
    t.prototype = {
        constructor: t,
        init: function(t, n, r) {
            var i, s, o, u, a;
            this.type = t;
            this.$element = e(n);
            this.options = this.getOptions(r);
            this.enabled = !0;
            o = this.options.trigger.split(" ");
            for (a = o.length; a--; ) {
                u = o[a];
                if (u == "click") this.$element.on("click." + this.type, this.options.selector, e.proxy(this.toggle, this)); else if (u != "manual") {
                    i = u == "hover" ? "mouseenter" : "focus";
                    s = u == "hover" ? "mouseleave" : "blur";
                    this.$element.on(i + "." + this.type, this.options.selector, e.proxy(this.enter, this));
                    this.$element.on(s + "." + this.type, this.options.selector, e.proxy(this.leave, this));
                }
            }
            this.options.selector ? this._options = e.extend({}, this.options, {
                trigger: "manual",
                selector: ""
            }) : this.fixTitle();
        },
        getOptions: function(t) {
            t = e.extend({}, e.fn[this.type].defaults, this.$element.data(), t);
            t.delay && typeof t.delay == "number" && (t.delay = {
                show: t.delay,
                hide: t.delay
            });
            return t;
        },
        enter: function(t) {
            var n = e.fn[this.type].defaults, r = {}, i;
            this._options && e.each(this._options, function(e, t) {
                n[e] != t && (r[e] = t);
            }, this);
            i = e(t.currentTarget)[this.type](r).data(this.type);
            if (!i.options.delay || !i.options.delay.show) return i.show();
            clearTimeout(this.timeout);
            i.hoverState = "in";
            this.timeout = setTimeout(function() {
                i.hoverState == "in" && i.show();
            }, i.options.delay.show);
        },
        leave: function(t) {
            var n = e(t.currentTarget)[this.type](this._options).data(this.type);
            this.timeout && clearTimeout(this.timeout);
            if (!n.options.delay || !n.options.delay.hide) return n.hide();
            n.hoverState = "out";
            this.timeout = setTimeout(function() {
                n.hoverState == "out" && n.hide();
            }, n.options.delay.hide);
        },
        show: function() {
            var t, n, r, i, s, o, u = e.Event("show");
            if (this.hasContent() && this.enabled) {
                this.$element.trigger(u);
                if (u.isDefaultPrevented()) return;
                t = this.tip();
                this.setContent();
                this.options.animation && t.addClass("fade");
                s = typeof this.options.placement == "function" ? this.options.placement.call(this, t[0], this.$element[0]) : this.options.placement;
                t.detach().css({
                    top: 0,
                    left: 0,
                    display: "block"
                });
                this.options.container ? t.appendTo(this.options.container) : t.insertAfter(this.$element);
                n = this.getPosition();
                r = t[0].offsetWidth;
                i = t[0].offsetHeight;
                switch (s) {
                  case "bottom":
                    o = {
                        top: n.top + n.height,
                        left: n.left + n.width / 2 - r / 2
                    };
                    break;
                  case "top":
                    o = {
                        top: n.top - i,
                        left: n.left + n.width / 2 - r / 2
                    };
                    break;
                  case "left":
                    o = {
                        top: n.top + n.height / 2 - i / 2,
                        left: n.left - r
                    };
                    break;
                  case "right":
                    o = {
                        top: n.top + n.height / 2 - i / 2,
                        left: n.left + n.width
                    };
                }
                this.applyPlacement(o, s);
                this.$element.trigger("shown");
            }
        },
        applyPlacement: function(e, t) {
            var n = this.tip(), r = n[0].offsetWidth, i = n[0].offsetHeight, s, o, u, a;
            n.offset(e).addClass(t).addClass("in");
            s = n[0].offsetWidth;
            o = n[0].offsetHeight;
            if (t == "top" && o != i) {
                e.top = e.top + i - o;
                a = !0;
            }
            if (t == "bottom" || t == "top") {
                u = 0;
                if (e.left < 0) {
                    u = e.left * -2;
                    e.left = 0;
                    n.offset(e);
                    s = n[0].offsetWidth;
                    o = n[0].offsetHeight;
                }
                this.replaceArrow(u - r + s, s, "left");
            } else this.replaceArrow(o - i, o, "top");
            a && n.offset(e);
        },
        replaceArrow: function(e, t, n) {
            this.arrow().css(n, e ? 50 * (1 - e / t) + "%" : "");
        },
        setContent: function() {
            var e = this.tip(), t = this.getTitle();
            e.find(".tooltip-inner")[this.options.html ? "html" : "text"](t);
            e.removeClass("fade in top bottom left right");
        },
        hide: function() {
            function i() {
                var t = setTimeout(function() {
                    n.off(e.support.transition.end).detach();
                }, 500);
                n.one(e.support.transition.end, function() {
                    clearTimeout(t);
                    n.detach();
                });
            }
            var t = this, n = this.tip(), r = e.Event("hide");
            this.$element.trigger(r);
            if (r.isDefaultPrevented()) return;
            n.removeClass("in");
            e.support.transition && this.$tip.hasClass("fade") ? i() : n.detach();
            this.$element.trigger("hidden");
            return this;
        },
        fixTitle: function() {
            var e = this.$element;
            (e.attr("title") || typeof e.attr("data-original-title") != "string") && e.attr("data-original-title", e.attr("title") || "").attr("title", "");
        },
        hasContent: function() {
            return this.getTitle();
        },
        getPosition: function() {
            var t = this.$element[0];
            return e.extend({}, typeof t.getBoundingClientRect == "function" ? t.getBoundingClientRect() : {
                width: t.offsetWidth,
                height: t.offsetHeight
            }, this.$element.offset());
        },
        getTitle: function() {
            var e, t = this.$element, n = this.options;
            e = t.attr("data-original-title") || (typeof n.title == "function" ? n.title.call(t[0]) : n.title);
            return e;
        },
        tip: function() {
            return this.$tip = this.$tip || e(this.options.template);
        },
        arrow: function() {
            return this.$arrow = this.$arrow || this.tip().find(".tooltip-arrow");
        },
        validate: function() {
            if (!this.$element[0].parentNode) {
                this.hide();
                this.$element = null;
                this.options = null;
            }
        },
        enable: function() {
            this.enabled = !0;
        },
        disable: function() {
            this.enabled = !1;
        },
        toggleEnabled: function() {
            this.enabled = !this.enabled;
        },
        toggle: function(t) {
            var n = t ? e(t.currentTarget)[this.type](this._options).data(this.type) : this;
            n.tip().hasClass("in") ? n.hide() : n.show();
        },
        destroy: function() {
            this.hide().$element.off("." + this.type).removeData(this.type);
        }
    };
    var n = e.fn.tooltip;
    e.fn.tooltip = function(n) {
        return this.each(function() {
            var r = e(this), i = r.data("tooltip"), s = typeof n == "object" && n;
            i || r.data("tooltip", i = new t(this, s));
            typeof n == "string" && i[n]();
        });
    };
    e.fn.tooltip.Constructor = t;
    e.fn.tooltip.defaults = {
        animation: !0,
        placement: "top",
        selector: !1,
        template: '<div class="tooltip"><div class="tooltip-arrow"></div><div class="tooltip-inner"></div></div>',
        trigger: "hover focus",
        title: "",
        delay: 0,
        html: !1,
        container: !1
    };
    e.fn.tooltip.noConflict = function() {
        e.fn.tooltip = n;
        return this;
    };
}(window.jQuery);

!function(e) {
    var t = function(e, t) {
        this.init("popover", e, t);
    };
    t.prototype = e.extend({}, e.fn.tooltip.Constructor.prototype, {
        constructor: t,
        setContent: function() {
            var e = this.tip(), t = this.getTitle(), n = this.getContent();
            e.find(".popover-title")[this.options.html ? "html" : "text"](t);
            e.find(".popover-content")[this.options.html ? "html" : "text"](n);
            e.removeClass("fade top bottom left right in");
        },
        hasContent: function() {
            return this.getTitle() || this.getContent();
        },
        getContent: function() {
            var e, t = this.$element, n = this.options;
            e = (typeof n.content == "function" ? n.content.call(t[0]) : n.content) || t.attr("data-content");
            return e;
        },
        tip: function() {
            this.$tip || (this.$tip = e(this.options.template));
            return this.$tip;
        },
        destroy: function() {
            this.hide().$element.off("." + this.type).removeData(this.type);
        }
    });
    var n = e.fn.popover;
    e.fn.popover = function(n) {
        return this.each(function() {
            var r = e(this), i = r.data("popover"), s = typeof n == "object" && n;
            i || r.data("popover", i = new t(this, s));
            typeof n == "string" && i[n]();
        });
    };
    e.fn.popover.Constructor = t;
    e.fn.popover.defaults = e.extend({}, e.fn.tooltip.defaults, {
        placement: "right",
        trigger: "click",
        content: "",
        template: '<div class="popover"><div class="arrow"></div><h3 class="popover-title"></h3><div class="popover-content"></div></div>'
    });
    e.fn.popover.noConflict = function() {
        e.fn.popover = n;
        return this;
    };
}(window.jQuery);

var hljs = new function() {
    function e(e) {
        return e.replace(/&/gm, "&amp;").replace(/</gm, "&lt;").replace(/>/gm, "&gt;");
    }
    function t(e) {
        for (var t = e.firstChild; t; t = t.nextSibling) {
            if (t.nodeName == "CODE") return t;
            if (t.nodeType != 3 || !t.nodeValue.match(/\s+/)) break;
        }
    }
    function n(e, t) {
        return Array.prototype.map.call(e.childNodes, function(e) {
            return e.nodeType == 3 ? t ? e.nodeValue.replace(/\n/g, "") : e.nodeValue : e.nodeName == "BR" ? "\n" : n(e, t);
        }).join("");
    }
    function r(e) {
        var t = (e.className + " " + e.parentNode.className).split(/\s+/);
        t = t.map(function(e) {
            return e.replace(/^language-/, "");
        });
        for (var n = 0; n < t.length; n++) if (p[t[n]] || t[n] == "no-highlight") return t[n];
    }
    function i(e) {
        var t = [];
        (function n(e, r) {
            for (var i = e.firstChild; i; i = i.nextSibling) if (i.nodeType == 3) r += i.nodeValue.length; else if (i.nodeName == "BR") r += 1; else if (i.nodeType == 1) {
                t.push({
                    event: "start",
                    offset: r,
                    node: i
                });
                r = n(i, r);
                t.push({
                    event: "stop",
                    offset: r,
                    node: i
                });
            }
            return r;
        })(e, 0);
        return t;
    }
    function s(t, n, r) {
        function u() {
            return t.length && n.length ? t[0].offset != n[0].offset ? t[0].offset < n[0].offset ? t : n : n[0].event == "start" ? t : n : t.length ? t : n;
        }
        function a(t) {
            function n(t) {
                return " " + t.nodeName + '="' + e(t.value) + '"';
            }
            return "<" + t.nodeName + Array.prototype.map.call(t.attributes, n).join("") + ">";
        }
        var i = 0, s = "", o = [];
        while (t.length || n.length) {
            var f = u().splice(0, 1)[0];
            s += e(r.substr(i, f.offset - i));
            i = f.offset;
            if (f.event == "start") {
                s += a(f.node);
                o.push(f.node);
            } else if (f.event == "stop") {
                var l, c = o.length;
                do {
                    c--;
                    l = o[c];
                    s += "</" + l.nodeName.toLowerCase() + ">";
                } while (l != f.node);
                o.splice(c, 1);
                while (c < o.length) {
                    s += a(o[c]);
                    c++;
                }
            }
        }
        return s + e(r.substr(i));
    }
    function o(e) {
        function t(t, n) {
            return RegExp(t, "m" + (e.cI ? "i" : "") + (n ? "g" : ""));
        }
        function n(e, r) {
            if (e.compiled) return;
            e.compiled = !0;
            var i = [];
            if (e.k) {
                var s = {};
                function o(e, t) {
                    t.split(" ").forEach(function(t) {
                        var n = t.split("|");
                        s[n[0]] = [ e, n[1] ? Number(n[1]) : 1 ];
                        i.push(n[0]);
                    });
                }
                e.lR = t(e.l || hljs.IR, !0);
                if (typeof e.k == "string") o("keyword", e.k); else for (var u in e.k) {
                    if (!e.k.hasOwnProperty(u)) continue;
                    o(u, e.k[u]);
                }
                e.k = s;
            }
            if (r) {
                e.bWK && (e.b = "\\b(" + i.join("|") + ")\\s");
                e.bR = t(e.b ? e.b : "\\B|\\b");
                !e.e && !e.eW && (e.e = "\\B|\\b");
                e.e && (e.eR = t(e.e));
                e.tE = e.e || "";
                e.eW && r.tE && (e.tE += (e.e ? "|" : "") + r.tE);
            }
            e.i && (e.iR = t(e.i));
            e.r === undefined && (e.r = 1);
            e.c || (e.c = []);
            for (var a = 0; a < e.c.length; a++) {
                e.c[a] == "self" && (e.c[a] = e);
                n(e.c[a], e);
            }
            e.starts && n(e.starts, r);
            var f = [];
            for (var a = 0; a < e.c.length; a++) f.push(e.c[a].b);
            e.tE && f.push(e.tE);
            e.i && f.push(e.i);
            e.t = f.length ? t(f.join("|"), !0) : {
                exec: function(e) {
                    return null;
                }
            };
        }
        n(e);
    }
    function u(t, n) {
        function r(e, t) {
            for (var n = 0; n < t.c.length; n++) {
                var r = t.c[n].bR.exec(e);
                if (r && r.index == 0) return t.c[n];
            }
        }
        function i(e, t) {
            if (e.e && e.eR.test(t)) return e;
            if (e.eW) return i(e.parent, t);
        }
        function s(e, t) {
            return t.i && t.iR.test(e);
        }
        function f(e, t) {
            var n = y.cI ? t[0].toLowerCase() : t[0];
            return e.k.hasOwnProperty(n) && e.k[n];
        }
        function l() {
            var t = e(w);
            if (!b.k) return t;
            var n = "", r = 0;
            b.lR.lastIndex = 0;
            var i = b.lR.exec(t);
            while (i) {
                n += t.substr(r, i.index - r);
                var s = f(b, i);
                if (s) {
                    S += s[1];
                    n += '<span class="' + s[0] + '">' + i[0] + "</span>";
                } else n += i[0];
                r = b.lR.lastIndex;
                i = b.lR.exec(t);
            }
            return n + t.substr(r);
        }
        function c() {
            if (b.sL && !p[b.sL]) return e(w);
            var t = b.sL ? u(b.sL, w) : a(w);
            if (b.r > 0) {
                S += t.keyword_count;
                E += t.r;
            }
            return '<span class="' + t.language + '">' + t.value + "</span>";
        }
        function h() {
            return b.sL !== undefined ? c() : l();
        }
        function v(t, n) {
            var r = t.cN ? '<span class="' + t.cN + '">' : "";
            if (t.rB) {
                x += r;
                w = "";
            } else if (t.eB) {
                x += e(n) + r;
                w = "";
            } else {
                x += r;
                w = n;
            }
            b = Object.create(t, {
                parent: {
                    value: b
                }
            });
            E += t.r;
        }
        function m(t, n) {
            w += t;
            if (n === undefined) {
                x += h();
                return 0;
            }
            var o = r(n, b);
            if (o) {
                x += h();
                v(o, n);
                return o.rB ? 0 : n.length;
            }
            var u = i(b, n);
            if (u) {
                !u.rE && !u.eE && (w += n);
                x += h();
                do {
                    b.cN && (x += "</span>");
                    b = b.parent;
                } while (b != u.parent);
                u.eE && (x += e(n));
                w = "";
                u.starts && v(u.starts, "");
                return u.rE ? 0 : n.length;
            }
            if (s(n, b)) throw "Illegal";
            w += n;
            return n.length || 1;
        }
        var y = p[t];
        o(y);
        var b = y, w = "", E = 0, S = 0, x = "";
        try {
            var T, N, C = 0;
            for (;;) {
                b.t.lastIndex = C;
                T = b.t.exec(n);
                if (!T) break;
                N = m(n.substr(C, T.index - C), T[0]);
                C = T.index + N;
            }
            m(n.substr(C));
            return {
                r: E,
                keyword_count: S,
                value: x,
                language: t
            };
        } catch (k) {
            if (k == "Illegal") return {
                r: 0,
                keyword_count: 0,
                value: e(n)
            };
            throw k;
        }
    }
    function a(t) {
        var n = {
            keyword_count: 0,
            r: 0,
            value: e(t)
        }, r = n;
        for (var i in p) {
            if (!p.hasOwnProperty(i)) continue;
            var s = u(i, t);
            s.language = i;
            s.keyword_count + s.r > r.keyword_count + r.r && (r = s);
            if (s.keyword_count + s.r > n.keyword_count + n.r) {
                r = n;
                n = s;
            }
        }
        r.language && (n.second_best = r);
        return n;
    }
    function f(e, t, n) {
        t && (e = e.replace(/^((<[^>]+>|\t)+)/gm, function(e, n, r, i) {
            return n.replace(/\t/g, t);
        }));
        n && (e = e.replace(/\n/g, "<br>"));
        return e;
    }
    function l(e, t, o) {
        var l = n(e, o), c = r(e);
        if (c == "no-highlight") return;
        var h = c ? u(c, l) : a(l);
        c = h.language;
        var p = i(e);
        if (p.length) {
            var v = document.createElement("pre");
            v.innerHTML = h.value;
            h.value = s(p, i(v), l);
        }
        h.value = f(h.value, t, o);
        var m = e.className;
        m.match("(\\s|^)(language-)?" + c + "(\\s|$)") || (m = m ? m + " " + c : c);
        e.innerHTML = h.value;
        e.className = m;
        e.result = {
            language: c,
            kw: h.keyword_count,
            re: h.r
        };
        h.second_best && (e.second_best = {
            language: h.second_best.language,
            kw: h.second_best.keyword_count,
            re: h.second_best.r
        });
    }
    function c() {
        if (c.called) return;
        c.called = !0;
        Array.prototype.map.call(document.getElementsByTagName("pre"), t).filter(Boolean).forEach(function(e) {
            l(e, hljs.tabReplace);
        });
    }
    function h() {
        window.addEventListener("DOMContentLoaded", c, !1);
        window.addEventListener("load", c, !1);
    }
    var p = {};
    this.LANGUAGES = p;
    this.highlight = u;
    this.highlightAuto = a;
    this.fixMarkup = f;
    this.highlightBlock = l;
    this.initHighlighting = c;
    this.initHighlightingOnLoad = h;
    this.IR = "[a-zA-Z][a-zA-Z0-9_]*";
    this.UIR = "[a-zA-Z_][a-zA-Z0-9_]*";
    this.NR = "\\b\\d+(\\.\\d+)?";
    this.CNR = "(\\b0[xX][a-fA-F0-9]+|(\\b\\d+(\\.\\d*)?|\\.\\d+)([eE][-+]?\\d+)?)";
    this.BNR = "\\b(0b[01]+)";
    this.RSR = "!|!=|!==|%|%=|&|&&|&=|\\*|\\*=|\\+|\\+=|,|\\.|-|-=|/|/=|:|;|<|<<|<<=|<=|=|==|===|>|>=|>>|>>=|>>>|>>>=|\\?|\\[|\\{|\\(|\\^|\\^=|\\||\\|=|\\|\\||~";
    this.BE = {
        b: "\\\\[\\s\\S]",
        r: 0
    };
    this.ASM = {
        cN: "string",
        b: "'",
        e: "'",
        i: "\\n",
        c: [ this.BE ],
        r: 0
    };
    this.QSM = {
        cN: "string",
        b: '"',
        e: '"',
        i: "\\n",
        c: [ this.BE ],
        r: 0
    };
    this.CLCM = {
        cN: "comment",
        b: "//",
        e: "$"
    };
    this.CBLCLM = {
        cN: "comment",
        b: "/\\*",
        e: "\\*/"
    };
    this.HCM = {
        cN: "comment",
        b: "#",
        e: "$"
    };
    this.NM = {
        cN: "number",
        b: this.NR,
        r: 0
    };
    this.CNM = {
        cN: "number",
        b: this.CNR,
        r: 0
    };
    this.BNM = {
        cN: "number",
        b: this.BNR,
        r: 0
    };
    this.inherit = function(e, t) {
        var n = {};
        for (var r in e) n[r] = e[r];
        if (t) for (var r in t) n[r] = t[r];
        return n;
    };
};

hljs.LANGUAGES.bash = function(e) {
    var t = "true false", n = "if then else elif fi for break continue while in do done echo exit return set declare", r = {
        cN: "variable",
        b: "\\$[a-zA-Z0-9_#]+"
    }, i = {
        cN: "variable",
        b: "\\${([^}]|\\\\})+}"
    }, s = {
        cN: "string",
        b: '"',
        e: '"',
        i: "\\n",
        c: [ e.BE, r, i ],
        r: 0
    }, o = {
        cN: "string",
        b: "'",
        e: "'",
        c: [ {
            b: "''"
        } ],
        r: 0
    }, u = {
        cN: "test_condition",
        b: "",
        e: "",
        c: [ s, o, r, i ],
        k: {
            literal: t
        },
        r: 0
    };
    return {
        k: {
            keyword: n,
            literal: t
        },
        c: [ {
            cN: "shebang",
            b: "(#!\\/bin\\/bash)|(#!\\/bin\\/sh)",
            r: 10
        }, r, i, e.HCM, s, o, e.inherit(u, {
            b: "\\[ ",
            e: " \\]",
            r: 0
        }), e.inherit(u, {
            b: "\\[\\[ ",
            e: " \\]\\]"
        }) ]
    };
}(hljs);

hljs.LANGUAGES.cs = function(e) {
    return {
        k: "abstract as base bool break byte case catch char checked class const continue decimal default delegate do double else enum event explicit extern false finally fixed float for foreach goto if implicit in int interface internal is lock long namespace new null object operator out override params private protected public readonly ref return sbyte sealed short sizeof stackalloc static string struct switch this throw true try typeof uint ulong unchecked unsafe ushort using virtual volatile void while ascending descending from get group into join let orderby partial select set value var where yield",
        c: [ {
            cN: "comment",
            b: "///",
            e: "$",
            rB: !0,
            c: [ {
                cN: "xmlDocTag",
                b: "///|<!--|-->"
            }, {
                cN: "xmlDocTag",
                b: "</?",
                e: ">"
            } ]
        }, e.CLCM, e.CBLCLM, {
            cN: "preprocessor",
            b: "#",
            e: "$",
            k: "if else elif endif define undef warning error line region endregion pragma checksum"
        }, {
            cN: "string",
            b: '@"',
            e: '"',
            c: [ {
                b: '""'
            } ]
        }, e.ASM, e.QSM, e.CNM ]
    };
}(hljs);

hljs.LANGUAGES.ruby = function(e) {
    var t = "[a-zA-Z_][a-zA-Z0-9_]*(\\!|\\?)?", n = "[a-zA-Z_]\\w*[!?=]?|[-+~]\\@|<<|>>|=~|===?|<=>|[<>]=?|\\*\\*|[-/+%^&*~`|]|\\[\\]=?", r = {
        keyword: "and false then defined module in return redo if BEGIN retry end for true self when next until do begin unless END rescue nil else break undef not super class case require yield alias while ensure elsif or include"
    }, i = {
        cN: "yardoctag",
        b: "@[A-Za-z]+"
    }, s = [ {
        cN: "comment",
        b: "#",
        e: "$",
        c: [ i ]
    }, {
        cN: "comment",
        b: "^\\=begin",
        e: "^\\=end",
        c: [ i ],
        r: 10
    }, {
        cN: "comment",
        b: "^__END__",
        e: "\\n$"
    } ], o = {
        cN: "subst",
        b: "#\\{",
        e: "}",
        l: t,
        k: r
    }, u = [ e.BE, o ], a = [ {
        cN: "string",
        b: "'",
        e: "'",
        c: u,
        r: 0
    }, {
        cN: "string",
        b: '"',
        e: '"',
        c: u,
        r: 0
    }, {
        cN: "string",
        b: "%[qw]?\\(",
        e: "\\)",
        c: u
    }, {
        cN: "string",
        b: "%[qw]?\\[",
        e: "\\]",
        c: u
    }, {
        cN: "string",
        b: "%[qw]?{",
        e: "}",
        c: u
    }, {
        cN: "string",
        b: "%[qw]?<",
        e: ">",
        c: u,
        r: 10
    }, {
        cN: "string",
        b: "%[qw]?/",
        e: "/",
        c: u,
        r: 10
    }, {
        cN: "string",
        b: "%[qw]?%",
        e: "%",
        c: u,
        r: 10
    }, {
        cN: "string",
        b: "%[qw]?-",
        e: "-",
        c: u,
        r: 10
    }, {
        cN: "string",
        b: "%[qw]?\\|",
        e: "\\|",
        c: u,
        r: 10
    } ], f = {
        cN: "function",
        bWK: !0,
        e: " |$|;",
        k: "def",
        c: [ {
            cN: "title",
            b: n,
            l: t,
            k: r
        }, {
            cN: "params",
            b: "\\(",
            e: "\\)",
            l: t,
            k: r
        } ].concat(s)
    }, l = s.concat(a.concat([ {
        cN: "class",
        bWK: !0,
        e: "$|;",
        k: "class module",
        c: [ {
            cN: "title",
            b: "[A-Za-z_]\\w*(::\\w+)*(\\?|\\!)?",
            r: 0
        }, {
            cN: "inheritance",
            b: "<\\s*",
            c: [ {
                cN: "parent",
                b: "(" + e.IR + "::)?" + e.IR
            } ]
        } ].concat(s)
    }, f, {
        cN: "constant",
        b: "(::)?(\\b[A-Z]\\w*(::)?)+",
        r: 0
    }, {
        cN: "symbol",
        b: ":",
        c: a.concat([ {
            b: n
        } ]),
        r: 0
    }, {
        cN: "symbol",
        b: t + ":",
        r: 0
    }, {
        cN: "number",
        b: "(\\b0[0-7_]+)|(\\b0x[0-9a-fA-F_]+)|(\\b[1-9][0-9_]*(\\.[0-9_]+)?)|[0_]\\b",
        r: 0
    }, {
        cN: "number",
        b: "\\?\\w"
    }, {
        cN: "variable",
        b: "(\\$\\W)|((\\$|\\@\\@?)(\\w+))"
    }, {
        b: "(" + e.RSR + ")\\s*",
        c: s.concat([ {
            cN: "regexp",
            b: "/",
            e: "/[a-z]*",
            i: "\\n",
            c: [ e.BE, o ]
        } ]),
        r: 0
    } ]));
    o.c = l;
    f.c[1].c = l;
    return {
        l: t,
        k: r,
        c: l
    };
}(hljs);

hljs.LANGUAGES.diff = function(e) {
    return {
        c: [ {
            cN: "chunk",
            b: "^\\@\\@ +\\-\\d+,\\d+ +\\+\\d+,\\d+ +\\@\\@$",
            r: 10
        }, {
            cN: "chunk",
            b: "^\\*\\*\\* +\\d+,\\d+ +\\*\\*\\*\\*$",
            r: 10
        }, {
            cN: "chunk",
            b: "^\\-\\-\\- +\\d+,\\d+ +\\-\\-\\-\\-$",
            r: 10
        }, {
            cN: "header",
            b: "Index: ",
            e: "$"
        }, {
            cN: "header",
            b: "=====",
            e: "=====$"
        }, {
            cN: "header",
            b: "^\\-\\-\\-",
            e: "$"
        }, {
            cN: "header",
            b: "^\\*{3} ",
            e: "$"
        }, {
            cN: "header",
            b: "^\\+\\+\\+",
            e: "$"
        }, {
            cN: "header",
            b: "\\*{5}",
            e: "\\*{5}$"
        }, {
            cN: "addition",
            b: "^\\+",
            e: "$"
        }, {
            cN: "deletion",
            b: "^\\-",
            e: "$"
        }, {
            cN: "change",
            b: "^\\!",
            e: "$"
        } ]
    };
}(hljs);

hljs.LANGUAGES.javascript = function(e) {
    return {
        k: {
            keyword: "in if for while finally var new function do return void else break catch instanceof with throw case default try this switch continue typeof delete let yield const",
            literal: "true false null undefined NaN Infinity"
        },
        c: [ e.ASM, e.QSM, e.CLCM, e.CBLCLM, e.CNM, {
            b: "(" + e.RSR + "|\\b(case|return|throw)\\b)\\s*",
            k: "return throw case",
            c: [ e.CLCM, e.CBLCLM, {
                cN: "regexp",
                b: "/",
                e: "/[gim]*",
                i: "\\n",
                c: [ {
                    b: "\\\\/"
                } ]
            }, {
                b: "<",
                e: ">;",
                sL: "xml"
            } ],
            r: 0
        }, {
            cN: "function",
            bWK: !0,
            e: "{",
            k: "function",
            c: [ {
                cN: "title",
                b: "[A-Za-z$_][0-9A-Za-z$_]*"
            }, {
                cN: "params",
                b: "\\(",
                e: "\\)",
                c: [ e.CLCM, e.CBLCLM ],
                i: "[\"'\\(]"
            } ],
            i: "\\[|%"
        } ]
    };
}(hljs);

hljs.LANGUAGES.lua = function(e) {
    var t = "\\[=*\\[", n = "\\]=*\\]", r = {
        b: t,
        e: n,
        c: [ "self" ]
    }, i = [ {
        cN: "comment",
        b: "--(?!" + t + ")",
        e: "$"
    }, {
        cN: "comment",
        b: "--" + t,
        e: n,
        c: [ r ],
        r: 10
    } ];
    return {
        l: e.UIR,
        k: {
            keyword: "and break do else elseif end false for if in local nil not or repeat return then true until while",
            built_in: "_G _VERSION assert collectgarbage dofile error getfenv getmetatable ipairs load loadfile loadstring module next pairs pcall print rawequal rawget rawset require select setfenv setmetatable tonumber tostring type unpack xpcall coroutine debug io math os package string table"
        },
        c: i.concat([ {
            cN: "function",
            bWK: !0,
            e: "\\)",
            k: "function",
            c: [ {
                cN: "title",
                b: "([_a-zA-Z]\\w*\\.)*([_a-zA-Z]\\w*:)?[_a-zA-Z]\\w*"
            }, {
                cN: "params",
                b: "\\(",
                eW: !0,
                c: i
            } ].concat(i)
        }, e.CNM, e.ASM, e.QSM, {
            cN: "string",
            b: t,
            e: n,
            c: [ r ],
            r: 10
        } ])
    };
}(hljs);

hljs.LANGUAGES.xml = function(e) {
    var t = "[A-Za-z0-9\\._:-]+", n = {
        eW: !0,
        c: [ {
            cN: "attribute",
            b: t,
            r: 0
        }, {
            b: '="',
            rB: !0,
            e: '"',
            c: [ {
                cN: "value",
                b: '"',
                eW: !0
            } ]
        }, {
            b: "='",
            rB: !0,
            e: "'",
            c: [ {
                cN: "value",
                b: "'",
                eW: !0
            } ]
        }, {
            b: "=",
            c: [ {
                cN: "value",
                b: "[^\\s/>]+"
            } ]
        } ]
    };
    return {
        cI: !0,
        c: [ {
            cN: "pi",
            b: "<\\?",
            e: "\\?>",
            r: 10
        }, {
            cN: "doctype",
            b: "<!DOCTYPE",
            e: ">",
            r: 10,
            c: [ {
                b: "\\[",
                e: "\\]"
            } ]
        }, {
            cN: "comment",
            b: "<!--",
            e: "-->",
            r: 10
        }, {
            cN: "cdata",
            b: "<\\!\\[CDATA\\[",
            e: "\\]\\]>",
            r: 10
        }, {
            cN: "tag",
            b: "<style(?=\\s|>|$)",
            e: ">",
            k: {
                title: "style"
            },
            c: [ n ],
            starts: {
                e: "</style>",
                rE: !0,
                sL: "css"
            }
        }, {
            cN: "tag",
            b: "<script(?=\\s|>|$)",
            e: ">",
            k: {
                title: "script"
            },
            c: [ n ],
            starts: {
                e: "</script>",
                rE: !0,
                sL: "javascript"
            }
        }, {
            b: "<%",
            e: "%>",
            sL: "vbscript"
        }, {
            cN: "tag",
            b: "</?",
            e: "/?>",
            c: [ {
                cN: "title",
                b: "[^ />]+"
            }, n ]
        } ]
    };
}(hljs);

hljs.LANGUAGES.markdown = function(e) {
    return {
        c: [ {
            cN: "header",
            b: "^#{1,3}",
            e: "$"
        }, {
            cN: "header",
            b: "^.+?\\n[=-]{2,}$"
        }, {
            b: "<",
            e: ">",
            sL: "xml",
            r: 0
        }, {
            cN: "bullet",
            b: "^([*+-]|(\\d+\\.))\\s+"
        }, {
            cN: "strong",
            b: "[*_]{2}.+?[*_]{2}"
        }, {
            cN: "emphasis",
            b: "\\*.+?\\*"
        }, {
            cN: "emphasis",
            b: "_.+?_",
            r: 0
        }, {
            cN: "blockquote",
            b: "^>\\s+",
            e: "$"
        }, {
            cN: "code",
            b: "`.+?`"
        }, {
            cN: "code",
            b: "^    ",
            e: "$",
            r: 0
        }, {
            cN: "horizontal_rule",
            b: "^-{3,}",
            e: "$"
        }, {
            b: "\\[.+?\\]\\(.+?\\)",
            rB: !0,
            c: [ {
                cN: "link_label",
                b: "\\[.+\\]"
            }, {
                cN: "link_url",
                b: "\\(",
                e: "\\)",
                eB: !0,
                eE: !0
            } ]
        } ]
    };
}(hljs);

hljs.LANGUAGES.css = function(e) {
    var t = {
        cN: "function",
        b: e.IR + "\\(",
        e: "\\)",
        c: [ e.NM, e.ASM, e.QSM ]
    };
    return {
        cI: !0,
        i: "[=/|']",
        c: [ e.CBLCLM, {
            cN: "id",
            b: "\\#[A-Za-z0-9_-]+"
        }, {
            cN: "class",
            b: "\\.[A-Za-z0-9_-]+",
            r: 0
        }, {
            cN: "attr_selector",
            b: "\\[",
            e: "\\]",
            i: "$"
        }, {
            cN: "pseudo",
            b: ":(:)?[a-zA-Z0-9\\_\\-\\+\\(\\)\\\"\\']+"
        }, {
            cN: "at_rule",
            b: "@(font-face|page)",
            l: "[a-z-]+",
            k: "font-face page"
        }, {
            cN: "at_rule",
            b: "@",
            e: "[{;]",
            eE: !0,
            k: "import page media charset",
            c: [ t, e.ASM, e.QSM, e.NM ]
        }, {
            cN: "tag",
            b: e.IR,
            r: 0
        }, {
            cN: "rules",
            b: "{",
            e: "}",
            i: "[^\\s]",
            r: 0,
            c: [ e.CBLCLM, {
                cN: "rule",
                b: "[^\\s]",
                rB: !0,
                e: ";",
                eW: !0,
                c: [ {
                    cN: "attribute",
                    b: "[A-Z\\_\\.\\-]+",
                    e: ":",
                    eE: !0,
                    i: "[^\\s]",
                    starts: {
                        cN: "value",
                        eW: !0,
                        eE: !0,
                        c: [ t, e.NM, e.QSM, e.ASM, e.CBLCLM, {
                            cN: "hexcolor",
                            b: "\\#[0-9A-F]+"
                        }, {
                            cN: "important",
                            b: "!important"
                        } ]
                    }
                } ]
            } ]
        } ]
    };
}(hljs);

hljs.LANGUAGES.http = function(e) {
    return {
        i: "\\S",
        c: [ {
            cN: "status",
            b: "^HTTP/[0-9\\.]+",
            e: "$",
            c: [ {
                cN: "number",
                b: "\\b\\d{3}\\b"
            } ]
        }, {
            cN: "request",
            b: "^[A-Z]+ (.*?) HTTP/[0-9\\.]+$",
            rB: !0,
            e: "$",
            c: [ {
                cN: "string",
                b: " ",
                e: " ",
                eB: !0,
                eE: !0
            } ]
        }, {
            cN: "attribute",
            b: "^\\w",
            e: ": ",
            eE: !0,
            i: "\\n|\\s|=",
            starts: {
                cN: "string",
                e: "$"
            }
        }, {
            b: "\\n\\n",
            starts: {
                sL: "",
                eW: !0
            }
        } ]
    };
}(hljs);

hljs.LANGUAGES.java = function(e) {
    return {
        k: "false synchronized int abstract float private char boolean static null if const for true while long throw strictfp finally protected import native final return void enum else break transient new catch instanceof byte super volatile case assert short package default double public try this switch continue throws",
        c: [ {
            cN: "javadoc",
            b: "/\\*\\*",
            e: "\\*/",
            c: [ {
                cN: "javadoctag",
                b: "@[A-Za-z]+"
            } ],
            r: 10
        }, e.CLCM, e.CBLCLM, e.ASM, e.QSM, {
            cN: "class",
            bWK: !0,
            e: "{",
            k: "class interface",
            i: ":",
            c: [ {
                bWK: !0,
                k: "extends implements",
                r: 10
            }, {
                cN: "title",
                b: e.UIR
            } ]
        }, e.CNM, {
            cN: "annotation",
            b: "@[A-Za-z]+"
        } ]
    };
}(hljs);

hljs.LANGUAGES.php = function(e) {
    var t = {
        cN: "variable",
        b: "\\$+[a-zA-Z_-ÿ][a-zA-Z0-9_-ÿ]*"
    }, n = [ e.inherit(e.ASM, {
        i: null
    }), e.inherit(e.QSM, {
        i: null
    }), {
        cN: "string",
        b: 'b"',
        e: '"',
        c: [ e.BE ]
    }, {
        cN: "string",
        b: "b'",
        e: "'",
        c: [ e.BE ]
    } ], r = [ e.BNM, e.CNM ], i = {
        cN: "title",
        b: e.UIR
    };
    return {
        cI: !0,
        k: "and include_once list abstract global private echo interface as static endswitch array null if endwhile or const for endforeach self var while isset public protected exit foreach throw elseif include __FILE__ empty require_once do xor return implements parent clone use __CLASS__ __LINE__ else break print eval new catch __METHOD__ case exception php_user_filter default die require __FUNCTION__ enddeclare final try this switch continue endfor endif declare unset true false namespace trait goto instanceof insteadof __DIR__ __NAMESPACE__ __halt_compiler",
        c: [ e.CLCM, e.HCM, {
            cN: "comment",
            b: "/\\*",
            e: "\\*/",
            c: [ {
                cN: "phpdoc",
                b: "\\s@[A-Za-z]+"
            } ]
        }, {
            cN: "comment",
            eB: !0,
            b: "__halt_compiler.+?;",
            eW: !0
        }, {
            cN: "string",
            b: "<<<['\"]?\\w+['\"]?$",
            e: "^\\w+;",
            c: [ e.BE ]
        }, {
            cN: "preprocessor",
            b: "<\\?php",
            r: 10
        }, {
            cN: "preprocessor",
            b: "\\?>"
        }, t, {
            cN: "function",
            bWK: !0,
            e: "{",
            k: "function",
            i: "\\$|\\[|%",
            c: [ i, {
                cN: "params",
                b: "\\(",
                e: "\\)",
                c: [ "self", t, e.CBLCLM ].concat(n).concat(r)
            } ]
        }, {
            cN: "class",
            bWK: !0,
            e: "{",
            k: "class",
            i: "[:\\(\\$]",
            c: [ {
                bWK: !0,
                eW: !0,
                k: "extends",
                c: [ i ]
            }, i ]
        }, {
            b: "=>"
        } ].concat(n).concat(r)
    };
}(hljs);

hljs.LANGUAGES.haskell = function(e) {
    var t = {
        cN: "type",
        b: "\\b[A-Z][\\w']*",
        r: 0
    }, n = {
        cN: "container",
        b: "\\(",
        e: "\\)",
        c: [ {
            cN: "type",
            b: "\\b[A-Z][\\w]*(\\((\\.\\.|,|\\w+)\\))?"
        }, {
            cN: "title",
            b: "[_a-z][\\w']*"
        } ]
    }, r = {
        cN: "container",
        b: "{",
        e: "}",
        c: n.c
    };
    return {
        k: "let in if then else case of where do module import hiding qualified type data newtype deriving class instance not as foreign ccall safe unsafe",
        c: [ {
            cN: "comment",
            b: "--",
            e: "$"
        }, {
            cN: "preprocessor",
            b: "{-#",
            e: "#-}"
        }, {
            cN: "comment",
            c: [ "self" ],
            b: "{-",
            e: "-}"
        }, {
            cN: "string",
            b: "\\s+'",
            e: "'",
            c: [ e.BE ],
            r: 0
        }, e.QSM, {
            cN: "import",
            b: "\\bimport",
            e: "$",
            k: "import qualified as hiding",
            c: [ n ],
            i: "\\W\\.|;"
        }, {
            cN: "module",
            b: "\\bmodule",
            e: "where",
            k: "module where",
            c: [ n ],
            i: "\\W\\.|;"
        }, {
            cN: "class",
            b: "\\b(class|instance)",
            e: "where",
            k: "class where instance",
            c: [ t ]
        }, {
            cN: "typedef",
            b: "\\b(data|(new)?type)",
            e: "$",
            k: "data type newtype deriving",
            c: [ t, n, r ]
        }, e.CNM, {
            cN: "shebang",
            b: "#!\\/usr\\/bin\\/env runhaskell",
            e: "$"
        }, t, {
            cN: "title",
            b: "^[_a-z][\\w']*"
        } ]
    };
}(hljs);

hljs.LANGUAGES.python = function(e) {
    var t = {
        cN: "prompt",
        b: "^(>>>|\\.\\.\\.) "
    }, n = [ {
        cN: "string",
        b: "(u|b)?r?'''",
        e: "'''",
        c: [ t ],
        r: 10
    }, {
        cN: "string",
        b: '(u|b)?r?"""',
        e: '"""',
        c: [ t ],
        r: 10
    }, {
        cN: "string",
        b: "(u|r|ur)'",
        e: "'",
        c: [ e.BE ],
        r: 10
    }, {
        cN: "string",
        b: '(u|r|ur)"',
        e: '"',
        c: [ e.BE ],
        r: 10
    }, {
        cN: "string",
        b: "(b|br)'",
        e: "'",
        c: [ e.BE ]
    }, {
        cN: "string",
        b: '(b|br)"',
        e: '"',
        c: [ e.BE ]
    } ].concat([ e.ASM, e.QSM ]), r = {
        cN: "title",
        b: e.UIR
    }, i = {
        cN: "params",
        b: "\\(",
        e: "\\)",
        c: [ "self", e.CNM, t ].concat(n)
    }, s = {
        bWK: !0,
        e: ":",
        i: "[${=;\\n]",
        c: [ r, i ],
        r: 10
    };
    return {
        k: {
            keyword: "and elif is global as in if from raise for except finally print import pass return exec else break not with class assert yield try while continue del or def lambda nonlocal|10",
            built_in: "None True False Ellipsis NotImplemented"
        },
        i: "(</|->|\\?)",
        c: n.concat([ t, e.HCM, e.inherit(s, {
            cN: "function",
            k: "def"
        }), e.inherit(s, {
            cN: "class",
            k: "class"
        }), e.CNM, {
            cN: "decorator",
            b: "@",
            e: "$"
        }, {
            b: "\\b(print|exec)\\("
        } ])
    };
}(hljs);

hljs.LANGUAGES.sql = function(e) {
    return {
        cI: !0,
        c: [ {
            cN: "operator",
            b: "(begin|start|commit|rollback|savepoint|lock|alter|create|drop|rename|call|delete|do|handler|insert|load|replace|select|truncate|update|set|show|pragma|grant)\\b(?!:)",
            e: ";",
            eW: !0,
            k: {
                keyword: "all partial global month current_timestamp using go revoke smallint indicator end-exec disconnect zone with character assertion to add current_user usage input local alter match collate real then rollback get read timestamp session_user not integer bit unique day minute desc insert execute like ilike|2 level decimal drop continue isolation found where constraints domain right national some module transaction relative second connect escape close system_user for deferred section cast current sqlstate allocate intersect deallocate numeric public preserve full goto initially asc no key output collation group by union session both last language constraint column of space foreign deferrable prior connection unknown action commit view or first into float year primary cascaded except restrict set references names table outer open select size are rows from prepare distinct leading create only next inner authorization schema corresponding option declare precision immediate else timezone_minute external varying translation true case exception join hour default double scroll value cursor descriptor values dec fetch procedure delete and false int is describe char as at in varchar null trailing any absolute current_time end grant privileges when cross check write current_date pad begin temporary exec time update catalog user sql date on identity timezone_hour natural whenever interval work order cascade diagnostics nchar having left call do handler load replace truncate start lock show pragma exists number",
                aggregate: "count sum min max avg"
            },
            c: [ {
                cN: "string",
                b: "'",
                e: "'",
                c: [ e.BE, {
                    b: "''"
                } ],
                r: 0
            }, {
                cN: "string",
                b: '"',
                e: '"',
                c: [ e.BE, {
                    b: '""'
                } ],
                r: 0
            }, {
                cN: "string",
                b: "`",
                e: "`",
                c: [ e.BE ]
            }, e.CNM ]
        }, e.CBLCLM, {
            cN: "comment",
            b: "--",
            e: "$"
        } ]
    };
}(hljs);

hljs.LANGUAGES.ini = function(e) {
    return {
        cI: !0,
        i: "[^\\s]",
        c: [ {
            cN: "comment",
            b: ";",
            e: "$"
        }, {
            cN: "title",
            b: "^\\[",
            e: "\\]"
        }, {
            cN: "setting",
            b: "^[a-z0-9\\[\\]_-]+[ \\t]*=[ \\t]*",
            e: "$",
            c: [ {
                cN: "value",
                eW: !0,
                k: "on off true false yes no",
                c: [ e.QSM, e.NM ]
            } ]
        } ]
    };
}(hljs);

hljs.LANGUAGES.perl = function(e) {
    var t = "getpwent getservent quotemeta msgrcv scalar kill dbmclose undef lc ma syswrite tr send umask sysopen shmwrite vec qx utime local oct semctl localtime readpipe do return format read sprintf dbmopen pop getpgrp not getpwnam rewinddir qqfileno qw endprotoent wait sethostent bless s|0 opendir continue each sleep endgrent shutdown dump chomp connect getsockname die socketpair close flock exists index shmgetsub for endpwent redo lstat msgctl setpgrp abs exit select print ref gethostbyaddr unshift fcntl syscall goto getnetbyaddr join gmtime symlink semget splice x|0 getpeername recv log setsockopt cos last reverse gethostbyname getgrnam study formline endhostent times chop length gethostent getnetent pack getprotoent getservbyname rand mkdir pos chmod y|0 substr endnetent printf next open msgsnd readdir use unlink getsockopt getpriority rindex wantarray hex system getservbyport endservent int chr untie rmdir prototype tell listen fork shmread ucfirst setprotoent else sysseek link getgrgid shmctl waitpid unpack getnetbyname reset chdir grep split require caller lcfirst until warn while values shift telldir getpwuid my getprotobynumber delete and sort uc defined srand accept package seekdir getprotobyname semop our rename seek if q|0 chroot sysread setpwent no crypt getc chown sqrt write setnetent setpriority foreach tie sin msgget map stat getlogin unless elsif truncate exec keys glob tied closedirioctl socket readlink eval xor readline binmode setservent eof ord bind alarm pipe atan2 getgrent exp time push setgrent gt lt or ne m|0 break given say state when", n = {
        cN: "subst",
        b: "[$@]\\{",
        e: "\\}",
        k: t,
        r: 10
    }, r = {
        cN: "variable",
        b: "\\$\\d"
    }, i = {
        cN: "variable",
        b: "[\\$\\%\\@\\*](\\^\\w\\b|#\\w+(\\:\\:\\w+)*|[^\\s\\w{]|{\\w+}|\\w+(\\:\\:\\w*)*)"
    }, s = [ e.BE, n, r, i ], o = {
        b: "->",
        c: [ {
            b: e.IR
        }, {
            b: "{",
            e: "}"
        } ]
    }, u = {
        cN: "comment",
        b: "^(__END__|__DATA__)",
        e: "\\n$",
        r: 5
    }, a = [ r, i, e.HCM, u, {
        cN: "comment",
        b: "^\\=\\w",
        e: "\\=cut",
        eW: !0
    }, o, {
        cN: "string",
        b: "q[qwxr]?\\s*\\(",
        e: "\\)",
        c: s,
        r: 5
    }, {
        cN: "string",
        b: "q[qwxr]?\\s*\\[",
        e: "\\]",
        c: s,
        r: 5
    }, {
        cN: "string",
        b: "q[qwxr]?\\s*\\{",
        e: "\\}",
        c: s,
        r: 5
    }, {
        cN: "string",
        b: "q[qwxr]?\\s*\\|",
        e: "\\|",
        c: s,
        r: 5
    }, {
        cN: "string",
        b: "q[qwxr]?\\s*\\<",
        e: "\\>",
        c: s,
        r: 5
    }, {
        cN: "string",
        b: "qw\\s+q",
        e: "q",
        c: s,
        r: 5
    }, {
        cN: "string",
        b: "'",
        e: "'",
        c: [ e.BE ],
        r: 0
    }, {
        cN: "string",
        b: '"',
        e: '"',
        c: s,
        r: 0
    }, {
        cN: "string",
        b: "`",
        e: "`",
        c: [ e.BE ]
    }, {
        cN: "string",
        b: "{\\w+}",
        r: 0
    }, {
        cN: "string",
        b: "-?\\w+\\s*\\=\\>",
        r: 0
    }, {
        cN: "number",
        b: "(\\b0[0-7_]+)|(\\b0x[0-9a-fA-F_]+)|(\\b[1-9][0-9_]*(\\.[0-9_]+)?)|[0_]\\b",
        r: 0
    }, {
        b: "(" + e.RSR + "|\\b(split|return|print|reverse|grep)\\b)\\s*",
        k: "split return print reverse grep",
        r: 0,
        c: [ e.HCM, u, {
            cN: "regexp",
            b: "(s|tr|y)/(\\\\.|[^/])*/(\\\\.|[^/])*/[a-z]*",
            r: 10
        }, {
            cN: "regexp",
            b: "(m|qr)?/",
            e: "/[a-z]*",
            c: [ e.BE ],
            r: 0
        } ]
    }, {
        cN: "sub",
        bWK: !0,
        e: "(\\s*\\(.*?\\))?[;{]",
        k: "sub",
        r: 5
    }, {
        cN: "operator",
        b: "-\\w\\b",
        r: 0
    } ];
    n.c = a;
    o.c[1].c = a;
    return {
        k: t,
        c: a
    };
}(hljs);

hljs.LANGUAGES.objectivec = function(e) {
    var t = {
        keyword: "int float while private char catch export sizeof typedef const struct for union unsigned long volatile static protected bool mutable if public do return goto void enum else break extern class asm case short default double throw register explicit signed typename try this switch continue wchar_t inline readonly assign property protocol self synchronized end synthesize id optional required implementation nonatomic interface super unichar finally dynamic IBOutlet IBAction selector strong weak readonly",
        literal: "false true FALSE TRUE nil YES NO NULL",
        built_in: "NSString NSDictionary CGRect CGPoint UIButton UILabel UITextView UIWebView MKMapView UISegmentedControl NSObject UITableViewDelegate UITableViewDataSource NSThread UIActivityIndicator UITabbar UIToolBar UIBarButtonItem UIImageView NSAutoreleasePool UITableView BOOL NSInteger CGFloat NSException NSLog NSMutableString NSMutableArray NSMutableDictionary NSURL NSIndexPath CGSize UITableViewCell UIView UIViewController UINavigationBar UINavigationController UITabBarController UIPopoverController UIPopoverControllerDelegate UIImage NSNumber UISearchBar NSFetchedResultsController NSFetchedResultsChangeType UIScrollView UIScrollViewDelegate UIEdgeInsets UIColor UIFont UIApplication NSNotFound NSNotificationCenter NSNotification UILocalNotification NSBundle NSFileManager NSTimeInterval NSDate NSCalendar NSUserDefaults UIWindow NSRange NSArray NSError NSURLRequest NSURLConnection class UIInterfaceOrientation MPMoviePlayerController dispatch_once_t dispatch_queue_t dispatch_sync dispatch_async dispatch_once"
    };
    return {
        k: t,
        i: "</",
        c: [ e.CLCM, e.CBLCLM, e.CNM, e.QSM, {
            cN: "string",
            b: "'",
            e: "[^\\\\]'",
            i: "[^\\\\][^']"
        }, {
            cN: "preprocessor",
            b: "#import",
            e: "$",
            c: [ {
                cN: "title",
                b: '"',
                e: '"'
            }, {
                cN: "title",
                b: "<",
                e: ">"
            } ]
        }, {
            cN: "preprocessor",
            b: "#",
            e: "$"
        }, {
            cN: "class",
            bWK: !0,
            e: "({|$)",
            k: "interface class protocol implementation",
            c: [ {
                cN: "id",
                b: e.UIR
            } ]
        }, {
            cN: "variable",
            b: "\\." + e.UIR
        } ]
    };
}(hljs);

hljs.LANGUAGES.coffeescript = function(e) {
    var t = {
        keyword: "in if for while finally new do return else break catch instanceof throw try this switch continue typeof delete debugger super then unless until loop of by when and or is isnt not",
        literal: "true false null undefined yes no on off ",
        reserved: "case default function var void with const let enum export import native __hasProp __extends __slice __bind __indexOf"
    }, n = "[A-Za-z$_][0-9A-Za-z$_]*", r = {
        cN: "title",
        b: n
    }, i = {
        cN: "subst",
        b: "#\\{",
        e: "}",
        k: t,
        c: [ e.BNM, e.CNM ]
    };
    return {
        k: t,
        c: [ e.BNM, e.CNM, e.ASM, {
            cN: "string",
            b: '"""',
            e: '"""',
            c: [ e.BE, i ]
        }, {
            cN: "string",
            b: '"',
            e: '"',
            c: [ e.BE, i ],
            r: 0
        }, {
            cN: "comment",
            b: "###",
            e: "###"
        }, e.HCM, {
            cN: "regexp",
            b: "///",
            e: "///",
            c: [ e.HCM ]
        }, {
            cN: "regexp",
            b: "//[gim]*"
        }, {
            cN: "regexp",
            b: "/\\S(\\\\.|[^\\n])*/[gim]*"
        }, {
            b: "`",
            e: "`",
            eB: !0,
            eE: !0,
            sL: "javascript"
        }, {
            cN: "function",
            b: n + "\\s*=\\s*(\\(.+\\))?\\s*[-=]>",
            rB: !0,
            c: [ r, {
                cN: "params",
                b: "\\(",
                e: "\\)"
            } ]
        }, {
            cN: "class",
            bWK: !0,
            k: "class",
            e: "$",
            i: ":",
            c: [ {
                bWK: !0,
                k: "extends",
                eW: !0,
                i: ":",
                c: [ r ]
            }, r ]
        }, {
            cN: "property",
            b: "@" + n
        } ]
    };
}(hljs);

hljs.LANGUAGES.nginx = function(e) {
    var t = [ {
        cN: "variable",
        b: "\\$\\d+"
    }, {
        cN: "variable",
        b: "\\${",
        e: "}"
    }, {
        cN: "variable",
        b: "[\\$\\@]" + e.UIR
    } ], n = {
        eW: !0,
        l: "[a-z/_]+",
        k: {
            built_in: "on off yes no true false none blocked debug info notice warn error crit select break last permanent redirect kqueue rtsig epoll poll /dev/poll"
        },
        r: 0,
        i: "=>",
        c: [ e.HCM, {
            cN: "string",
            b: '"',
            e: '"',
            c: [ e.BE ].concat(t),
            r: 0
        }, {
            cN: "string",
            b: "'",
            e: "'",
            c: [ e.BE ].concat(t),
            r: 0
        }, {
            cN: "url",
            b: "([a-z]+):/",
            e: "\\s",
            eW: !0,
            eE: !0
        }, {
            cN: "regexp",
            b: "\\s\\^",
            e: "\\s|{|;",
            rE: !0,
            c: [ e.BE ].concat(t)
        }, {
            cN: "regexp",
            b: "~\\*?\\s+",
            e: "\\s|{|;",
            rE: !0,
            c: [ e.BE ].concat(t)
        }, {
            cN: "regexp",
            b: "\\*(\\.[a-z\\-]+)+",
            c: [ e.BE ].concat(t)
        }, {
            cN: "regexp",
            b: "([a-z\\-]+\\.)+\\*",
            c: [ e.BE ].concat(t)
        }, {
            cN: "number",
            b: "\\b\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}(:\\d{1,5})?\\b"
        }, {
            cN: "number",
            b: "\\b\\d+[kKmMgGdshdwy]*\\b",
            r: 0
        } ].concat(t)
    };
    return {
        c: [ e.HCM, {
            b: e.UIR + "\\s",
            e: ";|{",
            rB: !0,
            c: [ {
                cN: "title",
                b: e.UIR,
                starts: n
            } ]
        } ],
        i: "[^\\s\\}]"
    };
}(hljs);

hljs.LANGUAGES.json = function(e) {
    var t = {
        literal: "true false null"
    }, n = [ e.QSM, e.CNM ], r = {
        cN: "value",
        e: ",",
        eW: !0,
        eE: !0,
        c: n,
        k: t
    }, i = {
        b: "{",
        e: "}",
        c: [ {
            cN: "attribute",
            b: '\\s*"',
            e: '"\\s*:\\s*',
            eB: !0,
            eE: !0,
            c: [ e.BE ],
            i: "\\n",
            starts: r
        } ],
        i: "\\S"
    }, s = {
        b: "\\[",
        e: "\\]",
        c: [ e.inherit(r, {
            cN: null
        }) ],
        i: "\\S"
    };
    n.splice(n.length, 0, i, s);
    return {
        c: n,
        k: t,
        i: "\\S"
    };
}(hljs);

hljs.LANGUAGES.django = function(e) {
    function t(e, t) {
        return t == undefined || !e.cN && t.cN == "tag" || e.cN == "value";
    }
    function n(e, r) {
        var s = {};
        for (var o in e) {
            o != "contains" && (s[o] = e[o]);
            var u = [];
            for (var a = 0; e.c && a < e.c.length; a++) u.push(n(e.c[a], e));
            t(e, r) && (u = i.concat(u));
            u.length && (s.c = u);
        }
        return s;
    }
    var r = {
        cN: "filter",
        b: "\\|[A-Za-z]+\\:?",
        eE: !0,
        k: "truncatewords removetags linebreaksbr yesno get_digit timesince random striptags filesizeformat escape linebreaks length_is ljust rjust cut urlize fix_ampersands title floatformat capfirst pprint divisibleby add make_list unordered_list urlencode timeuntil urlizetrunc wordcount stringformat linenumbers slice date dictsort dictsortreversed default_if_none pluralize lower join center default truncatewords_html upper length phone2numeric wordwrap time addslashes slugify first escapejs force_escape iriencode last safe safeseq truncatechars localize unlocalize localtime utc timezone",
        c: [ {
            cN: "argument",
            b: '"',
            e: '"'
        } ]
    }, i = [ {
        cN: "template_comment",
        b: "{%\\s*comment\\s*%}",
        e: "{%\\s*endcomment\\s*%}"
    }, {
        cN: "template_comment",
        b: "{#",
        e: "#}"
    }, {
        cN: "template_tag",
        b: "{%",
        e: "%}",
        k: "comment endcomment load templatetag ifchanged endifchanged if endif firstof for endfor in ifnotequal endifnotequal widthratio extends include spaceless endspaceless regroup by as ifequal endifequal ssi now with cycle url filter endfilter debug block endblock else autoescape endautoescape csrf_token empty elif endwith static trans blocktrans endblocktrans get_static_prefix get_media_prefix plural get_current_language language get_available_languages get_current_language_bidi get_language_info get_language_info_list localize endlocalize localtime endlocaltime timezone endtimezone get_current_timezone",
        c: [ r ]
    }, {
        cN: "variable",
        b: "{{",
        e: "}}",
        c: [ r ]
    } ], s = n(e.LANGUAGES.xml);
    s.cI = !0;
    return s;
}(hljs);

hljs.LANGUAGES.apache = function(e) {
    var t = {
        cN: "number",
        b: "[\\$%]\\d+"
    };
    return {
        cI: !0,
        k: {
            keyword: "acceptfilter acceptmutex acceptpathinfo accessfilename action addalt addaltbyencoding addaltbytype addcharset adddefaultcharset adddescription addencoding addhandler addicon addiconbyencoding addiconbytype addinputfilter addlanguage addmoduleinfo addoutputfilter addoutputfilterbytype addtype alias aliasmatch allow allowconnect allowencodedslashes allowoverride anonymous anonymous_logemail anonymous_mustgiveemail anonymous_nouserid anonymous_verifyemail authbasicauthoritative authbasicprovider authdbduserpwquery authdbduserrealmquery authdbmgroupfile authdbmtype authdbmuserfile authdefaultauthoritative authdigestalgorithm authdigestdomain authdigestnccheck authdigestnonceformat authdigestnoncelifetime authdigestprovider authdigestqop authdigestshmemsize authgroupfile authldapbinddn authldapbindpassword authldapcharsetconfig authldapcomparednonserver authldapdereferencealiases authldapgroupattribute authldapgroupattributeisdn authldapremoteuserattribute authldapremoteuserisdn authldapurl authname authnprovideralias authtype authuserfile authzdbmauthoritative authzdbmtype authzdefaultauthoritative authzgroupfileauthoritative authzldapauthoritative authzownerauthoritative authzuserauthoritative balancermember browsermatch browsermatchnocase bufferedlogs cachedefaultexpire cachedirlength cachedirlevels cachedisable cacheenable cachefile cacheignorecachecontrol cacheignoreheaders cacheignorenolastmod cacheignorequerystring cachelastmodifiedfactor cachemaxexpire cachemaxfilesize cacheminfilesize cachenegotiateddocs cacheroot cachestorenostore cachestoreprivate cgimapextension charsetdefault charsetoptions charsetsourceenc checkcaseonly checkspelling chrootdir contentdigest cookiedomain cookieexpires cookielog cookiename cookiestyle cookietracking coredumpdirectory customlog dav davdepthinfinity davgenericlockdb davlockdb davmintimeout dbdexptime dbdkeep dbdmax dbdmin dbdparams dbdpersist dbdpreparesql dbdriver defaulticon defaultlanguage defaulttype deflatebuffersize deflatecompressionlevel deflatefilternote deflatememlevel deflatewindowsize deny directoryindex directorymatch directoryslash documentroot dumpioinput dumpiologlevel dumpiooutput enableexceptionhook enablemmap enablesendfile errordocument errorlog example expiresactive expiresbytype expiresdefault extendedstatus extfilterdefine extfilteroptions fileetag filterchain filterdeclare filterprotocol filterprovider filtertrace forcelanguagepriority forcetype forensiclog gracefulshutdowntimeout group header headername hostnamelookups identitycheck identitychecktimeout imapbase imapdefault imapmenu include indexheadinsert indexignore indexoptions indexorderdefault indexstylesheet isapiappendlogtoerrors isapiappendlogtoquery isapicachefile isapifakeasync isapilognotsupported isapireadaheadbuffer keepalive keepalivetimeout languagepriority ldapcacheentries ldapcachettl ldapconnectiontimeout ldapopcacheentries ldapopcachettl ldapsharedcachefile ldapsharedcachesize ldaptrustedclientcert ldaptrustedglobalcert ldaptrustedmode ldapverifyservercert limitinternalrecursion limitrequestbody limitrequestfields limitrequestfieldsize limitrequestline limitxmlrequestbody listen listenbacklog loadfile loadmodule lockfile logformat loglevel maxclients maxkeepaliverequests maxmemfree maxrequestsperchild maxrequestsperthread maxspareservers maxsparethreads maxthreads mcachemaxobjectcount mcachemaxobjectsize mcachemaxstreamingbuffer mcacheminobjectsize mcacheremovalalgorithm mcachesize metadir metafiles metasuffix mimemagicfile minspareservers minsparethreads mmapfile mod_gzip_on mod_gzip_add_header_count mod_gzip_keep_workfiles mod_gzip_dechunk mod_gzip_min_http mod_gzip_minimum_file_size mod_gzip_maximum_file_size mod_gzip_maximum_inmem_size mod_gzip_temp_dir mod_gzip_item_include mod_gzip_item_exclude mod_gzip_command_version mod_gzip_can_negotiate mod_gzip_handle_methods mod_gzip_static_suffix mod_gzip_send_vary mod_gzip_update_static modmimeusepathinfo multiviewsmatch namevirtualhost noproxy nwssltrustedcerts nwsslupgradeable options order passenv pidfile protocolecho proxybadheader proxyblock proxydomain proxyerroroverride proxyftpdircharset proxyiobuffersize proxymaxforwards proxypass proxypassinterpolateenv proxypassmatch proxypassreverse proxypassreversecookiedomain proxypassreversecookiepath proxypreservehost proxyreceivebuffersize proxyremote proxyremotematch proxyrequests proxyset proxystatus proxytimeout proxyvia readmename receivebuffersize redirect redirectmatch redirectpermanent redirecttemp removecharset removeencoding removehandler removeinputfilter removelanguage removeoutputfilter removetype requestheader require rewritebase rewritecond rewriteengine rewritelock rewritelog rewriteloglevel rewritemap rewriteoptions rewriterule rlimitcpu rlimitmem rlimitnproc satisfy scoreboardfile script scriptalias scriptaliasmatch scriptinterpretersource scriptlog scriptlogbuffer scriptloglength scriptsock securelisten seerequesttail sendbuffersize serveradmin serveralias serverlimit servername serverpath serverroot serversignature servertokens setenv setenvif setenvifnocase sethandler setinputfilter setoutputfilter ssienableaccess ssiendtag ssierrormsg ssistarttag ssitimeformat ssiundefinedecho sslcacertificatefile sslcacertificatepath sslcadnrequestfile sslcadnrequestpath sslcarevocationfile sslcarevocationpath sslcertificatechainfile sslcertificatefile sslcertificatekeyfile sslciphersuite sslcryptodevice sslengine sslhonorciperorder sslmutex ssloptions sslpassphrasedialog sslprotocol sslproxycacertificatefile sslproxycacertificatepath sslproxycarevocationfile sslproxycarevocationpath sslproxyciphersuite sslproxyengine sslproxymachinecertificatefile sslproxymachinecertificatepath sslproxyprotocol sslproxyverify sslproxyverifydepth sslrandomseed sslrequire sslrequiressl sslsessioncache sslsessioncachetimeout sslusername sslverifyclient sslverifydepth startservers startthreads substitute suexecusergroup threadlimit threadsperchild threadstacksize timeout traceenable transferlog typesconfig unsetenv usecanonicalname usecanonicalphysicalport user userdir virtualdocumentroot virtualdocumentrootip virtualscriptalias virtualscriptaliasip win32disableacceptex xbithack",
            literal: "on off"
        },
        c: [ e.HCM, {
            cN: "sqbracket",
            b: "\\s\\[",
            e: "\\]$"
        }, {
            cN: "cbracket",
            b: "[\\$%]\\{",
            e: "\\}",
            c: [ "self", t ]
        }, t, {
            cN: "tag",
            b: "</?",
            e: ">"
        }, e.QSM ]
    };
}(hljs);

hljs.LANGUAGES.applescript = function(e) {
    var t = e.inherit(e.QSM, {
        i: ""
    }), n = {
        cN: "title",
        b: e.UIR
    }, r = {
        cN: "params",
        b: "\\(",
        e: "\\)",
        c: [ "self", e.CNM, t ]
    }, i = [ {
        cN: "comment",
        b: "--",
        e: "$"
    }, {
        cN: "comment",
        b: "\\(\\*",
        e: "\\*\\)",
        c: [ "self", {
            b: "--",
            e: "$"
        } ]
    }, e.HCM ];
    return {
        k: {
            keyword: "about above after against and around as at back before beginning behind below beneath beside between but by considering contain contains continue copy div does eighth else end equal equals error every exit fifth first for fourth from front get given global if ignoring in into is it its last local me middle mod my ninth not of on onto or over prop property put ref reference repeat returning script second set seventh since sixth some tell tenth that the then third through thru timeout times to transaction try until where while whose with without",
            constant: "AppleScript false linefeed return pi quote result space tab true",
            type: "alias application boolean class constant date file integer list number real record string text",
            command: "activate beep count delay launch log offset read round run say summarize write",
            property: "character characters contents day frontmost id item length month name paragraph paragraphs rest reverse running time version weekday word words year"
        },
        c: [ t, e.CNM, {
            cN: "type",
            b: "\\bPOSIX file\\b"
        }, {
            cN: "command",
            b: "\\b(clipboard info|the clipboard|info for|list (disks|folder)|mount volume|path to|(close|open for) access|(get|set) eof|current date|do shell script|get volume settings|random number|set volume|system attribute|system info|time to GMT|(load|run|store) script|scripting components|ASCII (character|number)|localized string|choose (application|color|file|file name|folder|from list|remote application|URL)|display (alert|dialog))\\b|^\\s*return\\b"
        }, {
            cN: "constant",
            b: "\\b(text item delimiters|current application|missing value)\\b"
        }, {
            cN: "keyword",
            b: "\\b(apart from|aside from|instead of|out of|greater than|isn't|(doesn't|does not) (equal|come before|come after|contain)|(greater|less) than( or equal)?|(starts?|ends|begins?) with|contained by|comes (before|after)|a (ref|reference))\\b"
        }, {
            cN: "property",
            b: "\\b(POSIX path|(date|time) string|quoted form)\\b"
        }, {
            cN: "function_start",
            bWK: !0,
            k: "on",
            i: "[${=;\\n]",
            c: [ n, r ]
        } ].concat(i)
    };
}(hljs);

hljs.LANGUAGES.cpp = function(e) {
    var t = {
        keyword: "false int float while private char catch export virtual operator sizeof dynamic_cast|10 typedef const_cast|10 const struct for static_cast|10 union namespace unsigned long throw volatile static protected bool template mutable if public friend do return goto auto void enum else break new extern using true class asm case typeid short reinterpret_cast|10 default double register explicit signed typename try this switch continue wchar_t inline delete alignof char16_t char32_t constexpr decltype noexcept nullptr static_assert thread_local restrict _Bool complex",
        built_in: "std string cin cout cerr clog stringstream istringstream ostringstream auto_ptr deque list queue stack vector map set bitset multiset multimap unordered_set unordered_map unordered_multiset unordered_multimap array shared_ptr"
    };
    return {
        k: t,
        i: "</",
        c: [ e.CLCM, e.CBLCLM, e.QSM, {
            cN: "string",
            b: "'\\\\?.",
            e: "'",
            i: "."
        }, {
            cN: "number",
            b: "\\b(\\d+(\\.\\d*)?|\\.\\d+)(u|U|l|L|ul|UL|f|F)"
        }, e.CNM, {
            cN: "preprocessor",
            b: "#",
            e: "$"
        }, {
            cN: "stl_container",
            b: "\\b(deque|list|queue|stack|vector|map|set|bitset|multiset|multimap|unordered_map|unordered_set|unordered_multiset|unordered_multimap|array)\\s*<",
            e: ">",
            k: t,
            r: 10,
            c: [ "self" ]
        } ]
    };
}(hljs);

var Holder = Holder || {};

(function(e, t) {
    function o(e, t) {
        var n = "complete", r = "readystatechange", i = !1, s = i, o = !0, u = e.document, a = u.documentElement, f = u.addEventListener ? "addEventListener" : "attachEvent", l = u.addEventListener ? "removeEventListener" : "detachEvent", c = u.addEventListener ? "" : "on", h = function(o) {
            (o.type != r || u.readyState == n) && ((o.type == "load" ? e : u)[l](c + o.type, h, i), !s && (s = !0) && t.call(e, null));
        }, p = function() {
            try {
                a.doScroll("left");
            } catch (e) {
                setTimeout(p, 50);
                return;
            }
            h("poll");
        };
        if (u.readyState == n) t.call(e, "lazy"); else {
            if (u.createEventObject && a.doScroll) {
                try {
                    o = !e.frameElement;
                } catch (d) {}
                o && p();
            }
            u[f](c + "DOMContentLoaded", h, i), u[f](c + r, h, i), e[f](c + "load", h, i);
        }
    }
    function u(e) {
        e = e.match(/^(\W)?(.*)/);
        var t = document["getElement" + (e[1] ? e[1] == "#" ? "ById" : "sByClassName" : "sByTagName")](e[2]), n = [];
        t != null && (t.length ? n = t : t.length == 0 ? n = t : n = [ t ]);
        return n;
    }
    function a(e, t) {
        var n = {};
        for (var r in e) n[r] = e[r];
        for (var i in t) n[i] = t[i];
        return n;
    }
    function f(e, t, n) {
        var r = [ t, e ].sort(), i = Math.round(r[1] / 16), s = Math.round(r[0] / 16), o = Math.max(n.size, i);
        return {
            height: o
        };
    }
    function l(e, t, n, r) {
        var i = f(t.width, t.height, n), o = i.height, u = t.width * r, a = t.height * r, l = n.font ? n.font : "sans-serif";
        s.width = u;
        s.height = a;
        e.textAlign = "center";
        e.textBaseline = "middle";
        e.fillStyle = n.background;
        e.fillRect(0, 0, u, a);
        e.fillStyle = n.foreground;
        e.font = "bold " + o + "px " + l;
        var c = n.text ? n.text : t.width + "x" + t.height;
        e.measureText(c).width / u > 1 && (o = n.size / (e.measureText(c).width / u));
        e.font = "bold " + o * r + "px " + l;
        e.fillText(c, u / 2, a / 2, u);
        return s.toDataURL("image/png");
    }
    function c(e, t, n, i) {
        var s = n.dimensions, o = n.theme, u = n.text ? decodeURIComponent(n.text) : n.text, f = s.width + "x" + s.height;
        o = u ? a(o, {
            text: u
        }) : o;
        o = n.font ? a(o, {
            font: n.font
        }) : o;
        var c = 1;
        window.devicePixelRatio && window.devicePixelRatio > 1 && (c = window.devicePixelRatio);
        if (e == "image") {
            t.setAttribute("data-src", i);
            t.setAttribute("alt", u ? u : o.text ? o.text + " [" + f + "]" : f);
            if (r || !n.auto) {
                t.style.width = s.width + "px";
                t.style.height = s.height + "px";
            }
            r ? t.style.backgroundColor = o.background : t.setAttribute("src", l(v, s, o, c));
        } else if (!r) {
            t.style.backgroundImage = "url(" + l(v, s, o, c) + ")";
            t.style.backgroundSize = s.width + "px " + s.height + "px";
        }
    }
    function h(e, t, n) {
        var r = t.dimensions, i = t.theme, s = t.text, o = r.width + "x" + r.height;
        i = s ? a(i, {
            text: s
        }) : i;
        var u = document.createElement("div");
        u.style.backgroundColor = i.background;
        u.style.color = i.foreground;
        u.className = e.className + " holderjs-fluid";
        u.style.width = t.dimensions.width + (t.dimensions.width.indexOf("%") > 0 ? "" : "px");
        u.style.height = t.dimensions.height + (t.dimensions.height.indexOf("%") > 0 ? "" : "px");
        u.id = e.id;
        e.style.width = 0;
        e.style.height = 0;
        if (i.text) u.appendChild(document.createTextNode(i.text)); else {
            u.appendChild(document.createTextNode(o));
            m.push(u);
            setTimeout(p, 0);
        }
        e.parentNode.insertBefore(u, e.nextSibling);
        window.jQuery && jQuery(function(t) {
            t(e).on("load", function() {
                e.style.width = u.style.width;
                e.style.height = u.style.height;
                t(e).show();
                t(u).remove();
            });
        });
    }
    function p() {
        for (i in m) {
            if (!m.hasOwnProperty(i)) continue;
            var e = m[i], t = e.firstChild;
            e.style.lineHeight = e.offsetHeight + "px";
            t.data = e.offsetWidth + "x" + e.offsetHeight;
        }
    }
    function d(t, n) {
        var r = {
            theme: g.themes.gray
        }, i = !1;
        for (sl = t.length, j = 0; j < sl; j++) {
            var s = t[j];
            if (e.flags.dimensions.match(s)) {
                i = !0;
                r.dimensions = e.flags.dimensions.output(s);
            } else if (e.flags.fluid.match(s)) {
                i = !0;
                r.dimensions = e.flags.fluid.output(s);
                r.fluid = !0;
            } else e.flags.colors.match(s) ? r.theme = e.flags.colors.output(s) : n.themes[s] ? r.theme = n.themes[s] : e.flags.text.match(s) ? r.text = e.flags.text.output(s) : e.flags.font.match(s) ? r.font = e.flags.font.output(s) : e.flags.auto.match(s) && (r.auto = !0);
        }
        return i ? r : !1;
    }
    var n = !1, r = !1, s = document.createElement("canvas");
    document.getElementsByClassName || (document.getElementsByClassName = function(e) {
        var t = document, n, r, i, s = [];
        if (t.querySelectorAll) return t.querySelectorAll("." + e);
        if (t.evaluate) {
            r = ".//*[contains(concat(' ', @class, ' '), ' " + e + " ')]", n = t.evaluate(r, t, null, 0, null);
            while (i = n.iterateNext()) s.push(i);
        } else {
            n = t.getElementsByTagName("*"), r = new RegExp("(^|\\s)" + e + "(\\s|$)");
            for (i = 0; i < n.length; i++) r.test(n[i].className) && s.push(n[i]);
        }
        return s;
    });
    window.getComputedStyle || (window.getComputedStyle = function(e, t) {
        return this.el = e, this.getPropertyValue = function(t) {
            var n = /(\-([a-z]){1})/g;
            return t == "float" && (t = "styleFloat"), n.test(t) && (t = t.replace(n, function() {
                return arguments[2].toUpperCase();
            })), e.currentStyle[t] ? e.currentStyle[t] : null;
        }, this;
    });
    Object.prototype.hasOwnProperty || (Object.prototype.hasOwnProperty = function(e) {
        var t = this.__proto__ || this.constructor.prototype;
        return e in this && (!(e in t) || t[e] !== this[e]);
    });
    if (!s.getContext) r = !0; else if (s.toDataURL("image/png").indexOf("data:image/png") < 0) r = !0; else var v = s.getContext("2d");
    var m = [], g = {
        domain: "holder.js",
        images: "img",
        bgnodes: ".holderjs",
        themes: {
            gray: {
                background: "#eee",
                foreground: "#aaa",
                size: 12
            },
            social: {
                background: "#3a5a97",
                foreground: "#fff",
                size: 12
            },
            industrial: {
                background: "#434A52",
                foreground: "#C2F200",
                size: 12
            }
        },
        stylesheet: ".holderjs-fluid {font-size:16px;font-weight:bold;text-align:center;font-family:sans-serif;margin:0}"
    };
    e.flags = {
        dimensions: {
            regex: /^(\d+)x(\d+)$/,
            output: function(e) {
                var t = this.regex.exec(e);
                return {
                    width: +t[1],
                    height: +t[2]
                };
            }
        },
        fluid: {
            regex: /^([0-9%]+)x([0-9%]+)$/,
            output: function(e) {
                var t = this.regex.exec(e);
                return {
                    width: t[1],
                    height: t[2]
                };
            }
        },
        colors: {
            regex: /#([0-9a-f]{3,})\:#([0-9a-f]{3,})/i,
            output: function(e) {
                var t = this.regex.exec(e);
                return {
                    size: g.themes.gray.size,
                    foreground: "#" + t[2],
                    background: "#" + t[1]
                };
            }
        },
        text: {
            regex: /text\:(.*)/,
            output: function(e) {
                return this.regex.exec(e)[1];
            }
        },
        font: {
            regex: /font\:(.*)/,
            output: function(e) {
                return this.regex.exec(e)[1];
            }
        },
        auto: {
            regex: /^auto$/
        }
    };
    for (var y in e.flags) {
        if (!e.flags.hasOwnProperty(y)) continue;
        e.flags[y].match = function(e) {
            return e.match(this.regex);
        };
    }
    e.add_theme = function(t, n) {
        t != null && n != null && (g.themes[t] = n);
        return e;
    };
    e.add_image = function(t, n) {
        var r = u(n);
        if (r.length) for (var i = 0, s = r.length; i < s; i++) {
            var o = document.createElement("img");
            o.setAttribute("data-src", t);
            r[i].appendChild(o);
        }
        return e;
    };
    e.run = function(t) {
        var r = a(g, t), i = [];
        r.images instanceof window.NodeList ? imageNodes = r.images : r.images instanceof window.Node ? imageNodes = [ r.images ] : imageNodes = u(r.images);
        r.elements instanceof window.NodeList ? bgnodes = r.bgnodes : r.bgnodes instanceof window.Node ? bgnodes = [ r.bgnodes ] : bgnodes = u(r.bgnodes);
        n = !0;
        for (l = 0, f = imageNodes.length; l < f; l++) i.push(imageNodes[l]);
        var s = document.getElementById("holderjs-style");
        if (!s) {
            s = document.createElement("style");
            s.setAttribute("id", "holderjs-style");
            s.type = "text/css";
            document.getElementsByTagName("head")[0].appendChild(s);
        }
        s.styleSheet ? s.styleSheet += r.stylesheet : s.textContent += r.stylesheet;
        var o = new RegExp(r.domain + '/(.*?)"?\\)');
        for (var f = bgnodes.length, l = 0; l < f; l++) {
            var p = window.getComputedStyle(bgnodes[l], null).getPropertyValue("background-image"), v = p.match(o);
            if (v) {
                var m = d(v[1].split("/"), r);
                m && c("background", bgnodes[l], m, p);
            }
        }
        for (var f = i.length, l = 0; l < f; l++) {
            var p = i[l].getAttribute("src") || i[l].getAttribute("data-src");
            if (p != null && p.indexOf(r.domain) >= 0) {
                var m = d(p.substr(p.lastIndexOf(r.domain) + r.domain.length + 1).split("/"), r);
                m && (m.fluid ? h(i[l], m, p) : c("image", i[l], m, p));
            }
        }
        return e;
    };
    o(t, function() {
        if (window.addEventListener) {
            window.addEventListener("resize", p, !1);
            window.addEventListener("orientationchange", p, !1);
        } else window.attachEvent("onresize", p);
        n || e.run();
    });
    typeof define == "function" && define.amd && define("Holder", [], function() {
        return e;
    });
})(Holder, window);

hljs.initHighlightingOnLoad();