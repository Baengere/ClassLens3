"use client"

import {useState} from 'react'
import {useRouter} from 'next/navigation'

export default function QuestionForm({assignmentId}){
    const router = useRouter();

    const [question, setQuestion] = useState("")
    const [marks, setMarks] = useState("")
    const [modelAnswer, setModelAnswer] = useState("")
    const [rubric, setRubric] = useState("")

    async function handleSubmit(e){
        e.preventDefault()

        const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/questions/`,
            {
                method:"POST",
                headers:{
                    "Content-Type":"application/json",
                },
                body:JSON.stringify({
                    assignment_id: Number(assignmentId),
                    question_text: question,
                    marks: Number(marks),
                    model_answer: modelAnswer,
                    rubric: rubric,

                })
            }
        )
        if (!response.ok){
            alert("Failed to create question");
            return;
        }
        router.push(`/assignments/${assignmentId}`);
        router.refresh();
    }
    return (
        <form onSubmit={handleSubmit} className='space-y-8'>
            <div>
                <label className='font-semibold'>Question</label>

                <textarea
                    className='w-full border rounded p-3 mt-3'
                    rows={4}
                    value={question}
                    onChange={(e)=>setQuestion(e.target.value)}
                />
            </div>
            <div>
                <label className='font-semibold'>Marks</label>
                <input
                    type='number'
                    className='w-full border rounded p-3 mt-2'
                    value={marks}
                    onChange={(e)=>setMarks(e.target.value)}
                />
            </div>
            <div>
                <label className='font-semibold'>Model Answer</label>
                <textarea
                    rows={6}
                    className='w-full border rounded p-3 mt-4'
                    value={modelAnswer}
                    onChange={(e)=>setModelAnswer(e.target.value)}
                />
            </div>
            <div>
                <label className='font-semibold'>Rubric</label>
                <textarea
                    rows={6}
                    placeholder={`
                        Definition (2)
                        Mentions sunlight (2)
                        Mentions water (2)
                        Mentions carbon dioxide (2)
                        Mentions glucose (2)
                        `}
                    className='w-full border rounded p-3 mt-2'
                    value={rubric}
                    onChange={(e)=>setRubric(e.target.value)}
                />
            </div>

            <button
            className='rounded bg-blue-600 px-6 py-3 text-white hover:bg-blue-700'>Save Question</button>
        </form>
    )
}