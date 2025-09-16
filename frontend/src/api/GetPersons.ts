import type { Person } from "./Models";

export async function GetPersons(page: number, limit: number, show_archived: boolean = false): Promise<Person[]> {

    let params = new URLSearchParams({
            page: page.toString(),
            limit: limit.toString(),
    })

    if (show_archived) {
        params.append("is_archived", "true")
    }

    const response = await fetch("/api/", {
        method: "POST",
        body: params
    })

    return await response.json() as Person[]

}