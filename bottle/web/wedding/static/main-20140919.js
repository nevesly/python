$(function(){var t=$("#widget-quote"),e="http://54.68.157.119/",n=window.localStorage,i=function(n){var i=Math.random()*n.length|0,o=n[i];if(t.find("a").prop({href:e+o.u,title:o.t}),t.find("p").text(o.d),window.configJiaThis){var a=window.jiathis_config;a.url=e+o.u,a.summary=o.d,a.title="#褪墨# 【"+o.t+"】"}},o="quotes",a="quotesUpdate",s=function(){$.getJSON("/static/quotes.json",function(t){i(t),n&&(n.setItem(o,JSON.stringify(t)),n.setItem(a,new Date))})};if(n&&n.getItem(o)){var r=new Date(n.getItem(a));new Date-r>1296e6?s():i(JSON.parse(n.getItem(o)))}else s();var c="active",u=$("#menuLink");u.on("click",function(){return u.toggleClass(c),$("#menu").toggleClass(c),$("#layout").toggleClass(c),!1});var g=function(t,e,n,i,o){e=1==e?"click":2==e?"middle-click":"right-click",ga("send","event",t,e,n),ga("send","pageview",{page:"/"+t+"/?u="+i,title:o})};$(".ad").on("mousedown",function(t){var e=$(this),n=e.find("img");g("ad",t.which,n.width()+"x"+n.height(),e.prop("href"),e.prop("title"))}),$("#widget-quote").on("mousedown","a",function(t){var e=$(this);g("widget",t.which,"quote",e.prop("href"),e.prop("title"))}),$(".post").on("mousedown","a",function(t){var e=$(this);g("outbound",t.which,"post-span",e.prop("href"),e.text())}),$("#search-form").on("submit",function(){ga("send","pageview","/search/?q="+encodeURIComponent($("#search-box").val()))})});
