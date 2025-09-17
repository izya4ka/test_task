<script setup lang="ts">
    import { ref, watch, type Ref} from 'vue';
    import { GetPersons } from '../../api/GetPersons';
    import type { Person } from '../../api/Models';

    const persons: Ref<Person[]> = ref([])

    const limit = ref(10)
    const loading = ref(true)
    const totalItems = ref(0)
    const page = ref(1)
    const headers = [
        { title: 'Имя', key: 'first_name', sortable: false, align: "center" as const},
        { title: 'Фамилия', key: 'last_name', sortable: false, align: "center" as const},
        { title: 'В архиве', key: 'is_archived', sortable: false, align: "center" as const},
        { title: 'Дата добавления', key: 'date_added', sortable: false, align: "center" as const},
    ]
    const showArchived = ref(false)

    const loadItems = ({ page, itemsPerPage }: {page: number, itemsPerPage: number}) => {
      loading.value = true
      GetPersons(page, itemsPerPage, showArchived.value).then(({items, total}) => {
        persons.value = items
        totalItems.value = total
        loading.value = false
      })
    }

    const getColor = (state: boolean): string => {
      return state ? "red" : "green"
    }

    const getText = (state: boolean): string => {
      return state ? "Да" : "Нет"
    }

    const formatTime = (date: string): string => {
      const new_date = new Date(date)
      return new_date.toLocaleDateString()
    }

    watch([showArchived], () => {
      loadItems({page: page.value, itemsPerPage: limit.value})
    })

</script>

<template>
    <v-card
      class="d-flex flex-column rounded-lg text-center justify-center align-center pa-8"
      title="Список участников проекта Разгром"
      >
        <v-data-table-server
          v-model:items-per-page="limit"
         :items="persons"
         :items-length="totalItems"
         :headers="headers"
         :loading="loading"
         v-model:page="page"
         item-value="id"
         @update:options="loadItems"
        >
          <template v-slot:item.is_archived="{ value }">
              <v-chip
                :border="`${getColor(value)} thin opacity-25`"
                :color="getColor(value)"
                :text="getText(value)"
                size="default"
              />
          </template>
          <template v-slot:item.date_added="{ value }">
              {{ formatTime(value) }}
          </template>
        </v-data-table-server>
        <div class="d-flex flex-row justify-space-between align-center w-100">
            <v-checkbox v-model="showArchived" color="pink" label="Отображать архивные записи" />
            <v-btn class="text-pink" to="/">
              Вернуться
            </v-btn>
        </div>
    </v-card>
</template>