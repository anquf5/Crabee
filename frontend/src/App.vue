<template>
  <div id="wrapper">
    <nav class="navbar is-dark is-fixed-top">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Crabee</strong></router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-end">
        <router-link to="/company" class="navbar-item">Company</router-link>
        <router-link to="/discussion" class="navbar-item">Discussion</router-link>
        <div class="navbar-item">
          <div class="buttons">
            <template v-if="$store.state.isLogin">
              <div class="buttons">
                <router-link to="/myaccount" class="button is-light">
                  <span class="icon-text">
                    <span class="icon">
                      <i class="fas fa-user"></i>
                    </span>
                    <span>My account</span>
                  </span>
                </router-link>
              </div>
            </template>
            <template v-else>
              <router-link to="/login" class="button is-light">
              <span class="icon-text">
                <span class="icon">
                  <i class="fas fa-user"></i>
                </span>
                <span>Log in</span>
              </span>
              </router-link>
            </template>
          </div>
        </div>
      </div>
    </nav>

    <section class="section">
      <div class="column col-8 is-centered">
        <router-view/>
      </div>
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2021</p>
    </footer>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      showMobileMenu: false,
      isRouterAlive: true
    }
  },
  beforeCreate() {
    this.$store.commit('init')

    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted() {

  },
  provide(){
    return {reload: this.reload}
  },
  methods: {
    reload(){
      this.isRouterAlive = false
      this.$nextTick(function (){
        this.isRouterAlive = true
      })
    }
  }
}
</script>
<style lang="scss">
@import '../node_modules/bulma';
</style>
