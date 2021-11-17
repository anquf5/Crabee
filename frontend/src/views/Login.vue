<template>
  <div class="log-in">
    <div class="columns is-centered">
      <div class="column is-4">
        <div class="box">
          <div class="content">
            <h1><strong>Log in</strong></h1>
          </div>
          <form @submit.prevent="loginSubmit">
            <div class="field mb-4">
              <p class="control has-icons-left has-icons-right">
                <input class="input" type="text" placeholder="Username" v-model="username">
                <span class="icon is-small is-left">
                  <i class="fas fa-user"></i>
                </span>
              </p>
            </div>
            <div class="field mb-4">
              <p class="control has-icons-left">
                <input class="input" type="password" placeholder="Password" v-model="password">
                <span class="icon is-small is-left">
                  <i class="fas fa-lock"></i>
                </span>
              </p>
            </div>
            <div class="field">
              <nav class="navbar">
                <div class="navbar-brand">
                  <div class="control">
                    <button class="button is-success"><strong>Log in</strong>
                    </button>
                  </div>
                </div>

                <div class="navbar-end">
                  <div class="navbar-item">
                    <router-link to="/signup">Click here&nbsp</router-link>to sign up!
                  </div>
                </div>
              </nav>
            </div>
          </form>
        </div>
      </div>
    </div>


  </div>

</template>

<script>
import axios from 'axios'
// import {Notification} from 'element-ui'
export default {
  name: "Login",
  data() {
    return {
        username: '',
        password: '',
    }
  },
  mounted() {
  },
  methods: {
    loginSubmit() {

      axios.defaults.headers.common["Authorization"] = ""
      localStorage.removeItem("token")

      const formData = {
        username: this.username,
        password: this.password
      }

      axios
        .post("/api/token/login/", formData)
        .then(response => {
          const token = response.data.auth_token

          this.$store.commit('setToken', token)

          axios.defaults.headers.common["Authorization"] = "Token" + token

          localStorage.setItem("token", token)

          // const toPath = this.$route.query.to || '/discussion';
          this.$router.push({path:"/"});

        })
        .catch(error => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`)
            }
          } else {
            this.errors.push('Something went wrong. Please try again')

            console.log(JSON.stringify(error))
          }
        })
    }
  }
}
</script>

<style scoped>

</style>
