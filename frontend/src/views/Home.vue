<template>
  <div class="home">
    <section class="section">
        <div class="columns is-multiline">
          <div class="column is-12">
            <p class="is-size-4 has-text-start mb-2"><strong>Explore Companies</strong></p>
          </div>
            <CompanyBox v-for="company in companies" v-bind:key="company.id" v-bind:company="company">
            </CompanyBox>
        </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import CompanyBox from "../components/CompanyBox.vue";

export default {
  name: 'Home',
  data() {
    return {
      companies: []
    }
  },
  components: {
    CompanyBox
  },
  mounted() {
    this.getCompanies()
  },
  methods: {
    getCompanies(){
      axios
        .get('/api/index_company/')
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
