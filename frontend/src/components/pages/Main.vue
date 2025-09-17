<script setup lang="ts">
  import { ref, onMounted, onUnmounted} from 'vue'
  import { router } from "../../plugins/routes"
  const current_time = ref(new Date())
  let interval = 0;
  onMounted(() => {
    current_time.value = new Date()

    interval = setInterval(() => {
      current_time.value = new Date()
    }, 1000)

  })

  onUnmounted(() => {
    clearInterval(interval)
  })

  const isDaytime = () => {
    let hours = current_time.value.getHours()
    return hours > 8 && hours < 21
  }

  const redirect = () => {
    if (isDaytime()) {
      router.push("/data")
    } else {
      router.push("/sleep")
    }
  }

</script>

<template>
    <v-card
      class="rounded-lg text-center"
      title="Время"
      subtitle="До реализации проекта Разгром"
    >
      <div class="pb-8 d-flex flex-column justify-center align-center">
        <p :class="[$vuetify.display.xs ? 'text-h2' : 'text-h1', 'mb-4']" style="font-family: 'Iosevka'">
          {{ current_time.toLocaleTimeString() }}
        </p>
        <v-btn class="text-pink" @click="redirect">
          Стать частью проекта
        </v-btn>
      </div>
    </v-card>
</template>

