import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Controll from '../views/Controll.vue'
import Setting from '../views/Setting.vue'

Vue.use(VueRouter)

const routes = [{
    path: '/',
    name: 'Home',
    component: Home
}, {
    path: '/controll',
    name: 'controll',
    component: Controll 
},{
    path: '/setting',
    name: 'setting',
    component: Setting
}]

const router = new VueRouter({
    routes
})

export default router