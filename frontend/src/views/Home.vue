<template>
  <div class="home">
    <section class="section">
        <form method="get" action="/search">
          <div class="field is-grouped mb-6">
            <p class="control is-expanded">
              <input class="input" type="text" placeholder="Input Company Name .." name="search">
            </p>
            <p class="control">
              <a class="button is-success">
            <span class="icon-text">
              <span class="icon">
                <i class="fas fa-search"></i>
              </span>
              <span>Search</span>
            </span>
              </a>
            </p>
          </div>
        </form>
        <div class="columns is-multiline">
          <div class="column is-12">
            <p class="is-size-4 has-text-start mb-2"><strong>Explore Companies</strong></p>
          </div>
          <div class="column is-4" v-for="company in companies" v-bind:key="company.id">
            <div class="box">
              <article class="media">
                <div class="media-left">
                  <figure class="image is-64x64">
                    <img src="https://media-exp1.licdn.com/dms/image/C560BAQHTvZwCx4p2Qg/company-logo_100_100/0/1612205615891?e=1645056000&v=beta&t=GQCAhBJWrUvKi2FCuKj6CspWqTp6OW_JQoKjQFr1fvc" alt="Image">
                  </figure>
                </div>
                <div class="media-content">
                  <div class="content">
                    <h4>
                      <strong>{{ company.name }}</strong>
                    </h4>
                    <p>Rate:{{ company.get_avg }}</p>
                    <p>{{ company.get_review_num }} reviews</p>
<!--                    <router-link to=  "company//\{{company.id}}" class="button is-dark mt-4">View details</router-link>-->
                  </div>
                </div>
              </article>
            </div>
          </div>
        </div>
    </section>



  </div>
</template>

<script>
import axios from 'axios'
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  data() {
    return {
      companies: []
    }
  },
  components: {

  },
  mounted() {
    this.getCompanies()
  },
  methods: {
    getCompanies(){
      axios
        .get('/api/company/')
        .then(response => {
          this.companies = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<style scoped>

</style>
