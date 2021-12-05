<template>
  <div class="column is-4">
    <router-link target="_blank" v-bind:to= "company.get_absolute_url">
      <div class="box">
        <article class="media">
          <div class="media-left">
            <figure class="image is-64x64">
              <img v-bind:src="company.get_image" alt="Image">
            </figure>
          </div>
          <div class="content">
            <h4>
              <strong>{{ company.name }}</strong>
            </h4>
            <p><star :size="36" :score="company.get_avg" :max_length="5"/></p>
            <p>{{ company.get_review_num }} reviews</p>
          </div>
        </article>
      </div>
    </router-link>
  </div>
</template>

<script>
import star from '../components/star.vue'
export default {
  name: "CompanyBox",
  components: {star},
  props: {
    company: Object
  },

}
</script>

<style scoped>

</style>
