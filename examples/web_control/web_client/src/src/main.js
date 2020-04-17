import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import fastClick from 'fastclick'
import './assets/styles/reset.css'
import './assets/styles/border.css'
import VueDialog from 'vue2-dialog'
import 'vue2-dialog/dist/VueDialog.css'
import './assets/font/NoirPro-BoldItalic.css'

Vue.config.productionTip = false
fastClick.attach(document.body)
Vue.use(VueDialog);
fastClick.prototype.focus = function (targetElement) {

    var length;
    var isIOS = !! navigator.userAgent.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/)

    //兼容处理:在iOS7中，有一些元素（如date、datetime、month等）在setSelectionRange会出现TypeError

    //这是因为这些元素并没有selectionStart和selectionEnd的整型数字属性，所以一旦引用就会报错，因此排除这些属性才使用setSelectionRange方法

    if (isIOS && targetElement.setSelectionRange && targetElement.type.indexOf('date') !== 0 && targetElement.type !== 'time' && targetElement.type !== 'month' && targetElement.type !== 'email') {

        length = targetElement.value.length;

        targetElement.setSelectionRange(length, length);

        /*修复bug ios 11.3不弹出键盘，这里加上聚焦代码，让其强制聚焦弹出键盘*/

        targetElement.focus();

    } else {

        targetElement.focus();

    }

};

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')