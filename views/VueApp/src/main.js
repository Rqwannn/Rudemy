// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import Vuex from './store'
import router from './router'
import IdleVue from 'idle-vue'
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';
// import 'bootstrap/dist/css/bootstrap.min.css'

import { library } from '@fortawesome/fontawesome-svg-core'
import { faTimesCircle } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faTimesCircle)

Vue.component('font-awesome-icon', FontAwesomeIcon)

const eventsHub = new Vue()

// idleTime sama seperti cookig jika lebih dari waktu yang di tentukan akan otomatis di redirect ke login

Vue.use(IdleVue, {
  eventEmitter: eventsHub,
  idleTime: 2880000
})

Vue.use(VueSweetalert2);

Vue.config.productionTip = false

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresLogin)) {
    if (!Vuex.getters.loggedIn) {
      next({ name: 'login' })
    } else {
      Vuex.state.SearchQuery = "";
      next()
    }
  } else {
    next()
  }
})

/* eslint-disable no-new */
new Vue({
  store: Vuex,
  router,
  render: h => h(App),
}).$mount('#app')

