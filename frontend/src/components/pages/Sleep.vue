<template>
    <v-main class="d-flex justify-center align-center fill-height pa-4">
    <v-card
      class="d-flex flex-column rounded-lg text-center justify-center align-center pa-8"
      :class="$vuetify.display.xs ? 'w-100' : ''"
      :style="{
        width: $vuetify.display.xs ? '100%' :
                  $vuetify.display.smAndDown || $vuetify.display.md ? '75%' : '50%'
      }">
        <p class="text-h1 mb-4">Иди спать!</p>
        <img src="../../../assets/storyteller.gif" class="mb-4"></img>
        <v-btn class="text-pink" to="/">
          Вернуться
        </v-btn>
    </v-card>
  </v-main>
</template>