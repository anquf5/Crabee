<template>
  <div class="myaccount">
    <section class="section">
      <div class="columns">
        <div class="column is-4">
          <div class="box">
            <div class="media">
              <div class="media-left">
                <figure class="image is-96x96">
                  <img src="../assets/default.jpg">
                </figure>
              </div>
              <div class="media-content ml-4">
                <div class="content">
                  <p class="is-size-5"><strong>Admin</strong></p>
                  <p class="is-size-6">University of Glasgow</p>
                  <button class="button has-background-info">
                    <strong class="has-text-white-bis">Edit Profile</strong>
                  </button>
                </div>
              </div>
            </div>

          </div>
        </div>
        <div class="column is-8">
          <div class="block">
            <p class="is-size-4 mb-4"><strong>My Discussion</strong></p>
            <div class="box" v-for="topic in topics" v-bind:key="topic.id">
              <router-link v-bind:to= "topic.get_absolute_url" class="columns">
                <div class="column is-6">
                  <p>{{ topic.title }}</p>
                </div>
                <div class="column is-4">
                  <p>Last Update: {{ topic.get_update_time }}</p>
                </div>
                <div class="column is-2">
                  <p>Reply: {{ topic.get_reply_num }}</p>
                </div>
              </router-link>
            </div>
          </div>
        </div>
      </div>



    </section>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "MyAccount",
  data(){
    return{
      topics:[],
    }
  },
  mounted() {
    this.getMyTopics()
  },
  methods:{
    getMyTopics(){
      axios
      .get('/api/mytopics/')
      .then(response => {
        this.topics = response.data
      })
      .catch(error => {
        console.log(error)
      })
    }
  }
}
</script>

<style lang="scss">

</style>
