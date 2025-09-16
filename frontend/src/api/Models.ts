export interface Person {
    id: number
    first_name: string
    last_name: string
    is_archived: boolean
    date_added: Date
}

export interface PostPerson {
    first_name: string,
    last_name: string,
    is_archived: boolean
}

export interface GetPersonsResponse {
    items: Person[]
    total: number
}