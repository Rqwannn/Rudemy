import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";
import { axios } from './axios-api'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState({
    storage: window.sessionStorage,
  })],
  state: {
     accessToken: null,
     refreshToken: null,
     message: "",
     SearchQuery: "",
     PaginationPrev: null,
     PaginationNext: null,
     APIData: [],
     StatusPaginate: '',
     Permissions: false,
     UserData: [],
     ActivePath: ''
  },
  mutations: {
    updateStorage (state, { access, refresh }) {
      state.accessToken = access
      state.refreshToken = refresh
    },
    destroyToken (state) {
      state.accessToken = null
      state.refreshToken = null
      state.Permissions = false
      state.UserData = []
    },
    updateMessage(state, { pesan }){
        state.message = pesan
    },
    updateUserAuth(state, { user }){
      state.UserData = user
      state.Permissions = true
    },
    setPath(state, { path }){
      state.ActivePath = path
    },
  },
  getters: {
    loggedIn (state) {
      return state.accessToken != null
    },
    message(state){
        return state.message
    },
  },
  actions: {
    userLogout (context) {
      if (context.getters.loggedIn) {
          context.commit('destroyToken')
      }
    },
    userLogin (context, usercredentials) {
      axios.post('/api/auth/', {
        username: usercredentials.username,
        password: usercredentials.password
      }).then(response => {
          if(response.data.status){
            context.commit('updateUserAuth', { user: response.data.UserData }) 
          } else {
            context.commit('updateMessage', {
              pesan: `${response.data.messages}`
            })
          }
      }).catch(err => {
        console.log(err)
      })

      return new Promise((resolve, reject) => {
        axios.post('/api/token/', {
          username: usercredentials.username,
          password: usercredentials.password
        })
          .then(response => {
            context.commit('updateStorage', { access: response.data.access, refresh: response.data.refresh }) 
            resolve()
          })
          .catch(err => {
            reject(err)
          })
      })
    },
    userRegis(context, usercredentials){
        return new Promise((resolve, reject) => {
            axios.post('api/register/', {
                first_name: usercredentials.first_name,
                email: usercredentials.email,
                username: usercredentials.username,
                password1: usercredentials.password1,
                password2: usercredentials.password2
            })
              .then(response => {
                context.commit('updateMessage', { pesan: response.data.message}) 
                resolve()
              })
              .catch(err => {
                reject(err)
              })
          })
        }
    }
})