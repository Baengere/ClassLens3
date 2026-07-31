"use client"
import { useState } from "react"

export default function AssignmentForm(){
    const [title, setTitle] = useState("")
    const [subject, setSubject] = useState("")
    const [description, setDescription] = useState("")

    async function handleSubmit(e){
        e.preventDefault()
        const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/assignments/`, {
            method: "POST",
            headers: {
                "Content-Type":"application/json",
            },
            body:JSON.stringify({
                title,
                subject,
                description
            }),
        });
        if(!response.ok){
            alert("Failed to create Assignment.")
            return;
        }
        setTitle("")
        setSubject("")
        setDescription("")

        alert("Assignment created!")
    }

    return (
        <form className="space-y-8" onSubmit={handleSubmit}>
            <div>
                <label>Title</label>
                <input
                    className="border w-full p-2 rounded"
                    value={title}
                    onChange={(e)=>setTitle(e.target.value)}
                />
            </div>
            <div>
                <label>Subject</label>
                <input
                    className="border w-full p-2 rounded"
                    value={subject}
                    onChange={(e)=>setSubject(e.target.value)}
                />
            </div>
            <div>
                <label>Description</label>
                <textarea
                    className="border w-full p-2 rounded"
                    value={description}
                    onChange={(e)=>setDescription(e.target.value)}
                />
            </div>
            <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded">Create Assignment</button>
        </form>
    )
}