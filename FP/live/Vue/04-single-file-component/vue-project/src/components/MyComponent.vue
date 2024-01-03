<template>
    <!-- div든 header든 최상위 요소는 하나만. 최상위요소에서 시작함. -->
    <div>
        <h2>My Component!</h2>
        <MyComponentItem />
        <MyComponentItem />
        <MyComponentItem />
    </div>
</template>

<script setup>
import MyComponentItem from './MyComponentItem.vue';

</script>

<style scoped>

</style>