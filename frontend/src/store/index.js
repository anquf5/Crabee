import { createStore } from 'vuex'

export default createStore({
  state: {
    isLogin: false,
    token: '',

  },
  mutations: {
    init(state){
      if(localStorage.getItem('token')){
        state.token = localStorage.getItem('token')
        state.isLogin = true
      } else {
        state.token = ''
        state.isLogin = false
      }
    },
    setToken(state, token) {
      state.token = token
      state.isLogin = true
    },
    removeToken(state){
      state.token = ''
      state.isLogin = false
    }
  },
  actions: {
  },
  modules: {
  }
})
