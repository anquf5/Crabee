<template>
  <div class="column col-4">
    <router-link target="_blank" v-bind:to= "company.get_absolute_url">
      <div class="box">
        <article class="media">
          <div class="media-left">
            <figure class="image is-64x64">
              <img v-bind:src="company.get_image" alt="Image">
            </figure>
          </div>
          <div class="media-content">
            <div class="content">
              <h4>
                <strong>{{ company.name }}</strong>
              </h4>
              <p>Rate:{{ company.get_avg }}</p>
              <p>{{ company.get_review_num }} reviews</p>
            </div>
          </div>
        </article>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "CompanyBox",
  props: {
    company: Object
  }
}
</script>

<style scoped>

</style>
