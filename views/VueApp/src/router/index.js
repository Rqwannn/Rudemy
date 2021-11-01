import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Page/Home'
import Login from '@/components/Page/Login'
import Register from '@/components/Page/Register'
import Logout from '@/components/Page/Logout'

Vue.use(Router)

const Url = 
    [
        {
            path: '/',
            name: 'Home',
            component: Home,
            meta: {
                requiresLogin: true
            }
        },
        {
            path: '/Login',
            name: 'login',
            component: Login,
        },
        {
            path: '/Register',
            name: 'Register',
            component: Register,
        },
        {
            path: '/Logout',
            name: 'logout',
            component: Logout,
        },
    ]

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: Url
})
