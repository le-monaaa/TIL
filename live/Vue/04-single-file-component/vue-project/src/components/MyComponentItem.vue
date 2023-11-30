<template>
    <div>
        <p>My Component Item</p>
        <input type="text" ref="input">

    </div>
</template>

<script setup>
import { ref, onMounted } from "vue"

// 이름과 변수명이 같아야 함
// ref()에 들어가는 값은 의미가 없음.
const input = ref()


onMounted(() => {
    console.log(input.value)

})
</script>

<style scoped>

</style>

