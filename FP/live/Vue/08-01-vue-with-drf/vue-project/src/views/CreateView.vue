<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <input type="text" v-model.trim="title">
      <textarea v-model.trim="content"></textarea>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue"
import { useCounterStore } from "../stores/counter";
import axios from "axios"
import { useRouter } from "vue-router";

const store = useCounterStore()
const router = useRouter()

const title = ref(null)
const content = ref(null)

const createArticle = function ( ){
  axios({
    method: "post",
    url: `${store.API_URL}/api/v1/articles/`,
    data:{
      title: title.value,
      content: content.value
    }
  })
  .then((res)=>{
    console.log(res)
    router.push({name:'ArticleView'})
  })
  .catch((err)=> {
    console.log(err)
  })
}

</script>

<style>

</style>
