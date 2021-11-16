<template>
  <div class="log-in">
    <div class="columns is-centered">
      <div class="column is-4">
        <div class="box">
          <div class="content">
            <h1><strong>Log in</strong></h1>
          </div>
          <form @submit.prevent="submit">
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
                    <router-link to="/sign-up">Click here</router-link>
                  </div>
                  <div class="navbar-item">to sign up!</div>
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
    document.title = 'Log in'
  },
  methods: {
    submit() {
      const formData = {
        username: this.username,
        password: this.password
      }

      axios
        .post("/api/user/login/", formData)
        .then(response => {
          if (response.data.msg === 1) {
            // const toPath = this.$route.query.to || '/discussion';
            this.$router.push({path:"/"});
          }
          // else {
          //   this.$notify({
          //     title:'Error',
          //     msg: 'response.data.msg'
          //   })
          // }

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
