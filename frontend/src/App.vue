<script setup>

</script>

<template>
  <v-app :theme="dark">
    <v-main class="d-flex justify-center align-center fill-height pa-4">
      <v-col cols="12" md="9" lg="6">
        <router-view />
      </v-col>
    </v-main>
  </v-app>
</template>