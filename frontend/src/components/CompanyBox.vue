<template>
  <div class="column col-4">
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