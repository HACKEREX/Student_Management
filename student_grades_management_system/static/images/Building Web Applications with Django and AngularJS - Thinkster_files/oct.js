twttr=window.twttr||{},twttr.conversion=function(){var t="https://analytics.twitter.com/i/adsct?p_id=Twitter&p_user_id=0",e="//t.co/i/adsct?p_id=Twitter&p_user_id=0";return{trackBase:function(t,e,n,r){if(e&&n){var a=t+"&merch_id="+encodeURIComponent(e);a+="&event="+encodeURIComponent(n),r&&(a+="&value="+encodeURIComponent(r)),this.buildPixel(a)}},trackPidBase:function(t,e,n){if(e){var r="undefined"!=typeof n&&n.tw_sale_amount?encodeURIComponent(n.tw_sale_amount):0,a="undefined"!=typeof n&&n.tw_order_quantity?encodeURIComponent(n.tw_order_quantity):0,i=t+"&txn_id="+encodeURIComponent(e)+"&tw_sale_amount="+r+"&tw_order_quantity="+a,o=this.getIframeStatus();if(i+="&tw_iframe_status="+encodeURIComponent(o.value),o===this.IframeStatusCodes.IN_IFRAME&&""!=document.referrer){var s=encodeURIComponent(document.referrer);i+="&tw_document_referrer="+s}this.buildPixel(i)}},track:function(n,r,a){this.trackBase(t,n,r,a),this.trackBase(e,n,r,a)},trackPid:function(n,r){this.trackPidBase(t,n,r),this.trackPidBase(e,n,r)},buildPixel:function(t){var e=new Image;e.src=t},getIframeStatus:function(){try{return this.isIframed()?this.IframeStatusCodes.NOT_IN_IFRAME:this.IframeStatusCodes.IN_IFRAME}catch(t){return this.IframeStatusCodes.ERROR}},isIframed:function(){return window.self===window.top},IframeStatusCodes:{NOT_IN_IFRAME:{value:0},IN_IFRAME:{value:1},ERROR:{value:2}}}}();