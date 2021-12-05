<template>
  <div>
    <div class="star" :class="rate">
      <span class="star-item mt-1" v-for = "itemClass in starRate" :class="itemClass"></span>
      <span class="ml-3">{{this.score}}</span>
    </div>
  </div>
</template>

<script>
const CLS_ON = "on";
const CLS_HALF = "half";
const CLS_OFF = "off";
export default {
  name: "star",
  props: {
    size: {
      type : Number
    },
    score: {
      type : Number
    },
    showText: {
      type: Boolean,
      default: false,
    },
    max_length: {
      type : Number
    }
  },
  computed: {
    rate(){
      return "star-" + this.size;
    },
    starRate(){
      const result = [];
      let score = this.score;
      let max_length = this.max_length;
      let onstar = parseInt(this.score);
      let hasDecimal = score % 1 !==0;
      for(let i = 0; i < onstar; i++){
        result.push(CLS_ON);
      }
      if(hasDecimal){
        result.push(CLS_HALF);
      }
      while(result.length < max_length){
        result.push(CLS_OFF);
      }
      return result;
    }
  }
}
</script>
<style scoped>
.star {
  display: flex;
  width: 100%;
}
.star-36 .star-item {
  width: 15px;
  height: 15px;
  margin-right: 6px;
  background-repeat: no-repeat;
  background-size: 15px 15px;
}
.star-36 .star-item:last-child {
  margin-right: 0px;
}
.star-36 .star-item:last-child {
  margin-right: 0px;
}
.star-36 .star-item.on {
  background-image: url("../assets/on.png");
}
.star-36 .star-item.half {
  background-image: url("../assets/half.png");
}
.star-36 .star-item.off {
  background-image: url("../assets/off.png");
}
</style>
