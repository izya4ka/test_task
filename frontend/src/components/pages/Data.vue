<script setup lang="ts">
    import { onMounted, reactive } from 'vue';
    import type { Person } from '../../api/Models';
import { GetPersons } from '../../api/GetPersons';

    let persons: Person[] = reactive([])

    onMounted(async () => {
        (await GetPersons(0, 10)).forEach((person) => {
            persons.push(person)
        })
    })

</script>

<template>
    <v-main class="d-flex justify-center align-center fill-height pa-4">
    <v-card
      class="d-flex flex-column rounded-lg text-center justify-center align-center pa-8"
      title="Список участников проекта Разгром"
      :class="$vuetify.display.xs ? 'w-100' : ''"
      :style="{
        width: $vuetify.display.xs ? '100%' :
                  $vuetify.display.smAndDown || $vuetify.display.md ? '75%' : '50%'
      }">
        <v-data-table :items="persons">
            
        </v-data-table>
        <div class="d-flex flex-row-reverse w-100">
            <v-btn to="/">
            Вернуться
            </v-btn>
        </div>
    </v-card>
  </v-main>
</template>