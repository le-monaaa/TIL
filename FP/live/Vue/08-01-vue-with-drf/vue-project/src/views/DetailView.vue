<template>
  <div>
    <h1>Detail</h1>
    <div v-if="article">
      <p> {{ article.title }} </p>
      <p> {{ article.content }} </p>
      <p> {{ article.created_at }} </p>
      <p> {{ article.updated_at }} </p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted } from 'vue';
import { useCounterStore } from '../stores/counter';
import { useRoute } from 'vue-router';
import { ref } from "vue"

const store = useCounterStore()
const route = useRoute()

const article = ref(null)
onMounted(()=> {
  axios({
    method: "get",
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`
  })
  .then((res)=>{
    console.log(res.data)
    article.value = res.data
  })
  .catch((err)=>{
    console.log(err)
  })
})

</script>

<style>

</style>
