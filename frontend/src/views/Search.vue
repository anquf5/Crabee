<template>
  <div class="search">
      <form method="get" action="/search">
        <div class="field is-grouped mb-6">
          <div class="control is-expanded">
            <input class="input" type="text" placeholder="Input Company Name .." name="query">
          </div>
          <div class="control">
            <button class="button is-success">
                <span class="icon-text">
                  <span class="icon">
                    <i class="fas fa-search"></i>
                  </span>
                  <span>Search</span>
                </span>
            </button>
          </div>
        </div>
      </form>
    <div class="columns is-multiline">
      <div class="column is-12">
        <p class="is-size-4 has-text-start mb-2"><strong>Search results about "{{ query }}"</strong></p>
      </div>
      <CompanyBox v-for="company in companies" v-bind:key="company.id" v-bind:company="company">
      </CompanyBox>
    </div>
  </div>

</template>

<script>
import axios from 'axios'
import CompanyBox from "../components/CompanyBox";

export default {
  name: "Search",
  components: {
    CompanyBox
  },
  data() {
    return {
      companies: [],
      query: ''
    }
  },
  mounted() {
    let uri = window.location.search.substring(1)
    let params = new URLSearchParams(uri)

    if (params.get('query')) {
      this.query = params.get('query')

      this.search()
    }
  },
  methods: {
    search() {
      axios
          .post('/api/company/search/', {'query': this.query})
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
