import type { GetPersonsResponse } from "./Models";

export async function GetPersons(page: number, limit: number, show_archived: boolean = false): Promise<GetPersonsResponse> {

    let params = new URLSearchParams({
            page: page.toString(),
            limit: limit.toString(),
    })

    if (show_archived) {
        params.append("show_archived", "true")
    }

    const response = await fetch(("/api/persons?" + params).toString(), {
        method: "GET",
    })

    let result = await response.json() as GetPersonsResponse

    return result

}