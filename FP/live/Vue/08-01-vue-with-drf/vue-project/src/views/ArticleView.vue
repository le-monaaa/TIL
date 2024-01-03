<template>
  <div>
    <h1>Article Page</h1>
    <RouterLink :to="{name:'CreateView'}">
    [CREATE]
    </RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
import ArticleList from "@/components/ArticleList.vue"
import { onMounted } from "vue";
import { useCounterStore } from "@/stores/counter";
import { RouterLink } from "vue-router";

const store = useCounterStore()

// mount 될 때 실행하겠다.
onMounted(()=> {
  store.getArticles()
})
</script>

<style>

</style>
