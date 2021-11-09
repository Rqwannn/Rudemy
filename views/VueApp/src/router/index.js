import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Page/Home'
import Course from '@/components/Page/Course'
import Account from '@/components/Page/Account'
import Inbox from '@/components/Page/Inbox'
import UserProfile from '@/components/Page/UserProfile'
import UserCourse from '@/components/Page/UserCourse'
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
            path: '/Course',
            name: 'Course',
            component: Course,
            meta: {
                requiresLogin: true
            }
        },
        {
            path: '/Account',
            name: 'Account',
            component: Account,
            meta: {
                requiresLogin: true
            }
        },
        {
            path: '/Inbox',
            name: 'Inbox',
            component: Inbox,
            meta: {
                requiresLogin: true
            }
        },
        {
            path: '/UserProfile/:id',
            name: 'UserProfile',
            component: UserProfile,
            props: true,
            meta: {
                requiresLogin: true
            }
        },
        {
            path: '/UserCourse/:id',
            name: 'UserCourse',
            component: UserCourse,
            props: true,
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
