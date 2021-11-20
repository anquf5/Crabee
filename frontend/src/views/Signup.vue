<template>
  <div class="sign-up">
    <div class="columns is-centered">
      <div class="column is-4">
        <div class="box">
          <div class="content">
            <h1><strong>Signup</strong></h1>
          </div>
          <form @submit.prevent="signupSubmit">
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
            <div class="field mb-4">
              <p class="control has-icons-left">
                <input class="input" type="password" placeholder="Input password again" v-model="password_v">
                <span class="icon is-small is-left">
                  <i class="fas fa-lock"></i>
                </span>
              </p>
            </div>
            <div class="field mb-4">
              <p class="control has-icons-left">
                <input class="input" type="email" placeholder="Email" v-model="email">
                <span class="icon is-small is-left">
                  <i class="fas fa-envelope"></i>
                </span>
              </p>
            </div>

            <div class="notification is-danger" v-if="errors.length">
              <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>

            <div class="field">
              <div class="control">
                <button class="button is-success"><strong>Sign up</strong>
                </button>
              </div>
              <div class="is-divider" data-content="OR"></div>
              Have an account? <router-link to="/login">Click here</router-link> to login!
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import {toast} from "bulma-toast";
import { devided } from 'bulma-divider';
// import {Notification} from 'element-ui'
export default {
  name: "Signup",
  data() {
    return {
      username: '',
      password: '',
      password_v: '',
      email: '',
      errors:[],
    }
  },
  mounted() {
  },
  methods: {
    signupSubmit() {
      this.errors = []

      if (this.username === '') {
        this.errors.push('Username is required!')
      }

      if (this.password === '' || this.password.length <= 8) {
        this.errors.push('Password should be at least 8 characters!')
      }

      if (this.password_v !== this.password) {
        this.errors.push('The passwords doesn\'t match')
      }

      if (this.email === '') {
        this.errors.push('Email is required!')
      }

      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password
        }

        axios
            .post("/api/users/", formData)
            .then(response => {
              toast({
                message: 'Account created, please log in!',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
              })

              this.$router.push('/login')
            })
            .catch(error => {
              if (error.response) {
                for (const property in error.response.data) {
                  this.errors.push(`${property}: ${error.response.data[property]}`)
                }

                console.log(JSON.stringify(error.response.data))
              } else if (error.message) {
                this.errors.push('Something went wrong. Please try again')

                console.log(JSON.stringify(error))
              }
            })
      }
    }
  }
}
</script>

<style scoped>

</style>
