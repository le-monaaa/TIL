<template>
  <div>
    <h1>Sign up</h1>
    <form @submit.prevent="signup">
      <input type="text" v-model="username">
      <input type="password" v-model="password1">
      <input type="password" v-model="password2">
      <button type="submit">제출</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue"
import { useCounterStore} from "@/stores/counter"

const store = useCounterStore()

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const signup = function(){
  const payload = {
    username : username.value,
    password1 : password1.value,
    password2 : password2.value
  }
  store.signUp(payload)
}

</script>

<style>

</style>
