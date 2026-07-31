"use client"

import {useState} from 'react'
import {useRouter} from 'next/navigation'

export default function ReviewPanel({submission}){
    const router = useRouter()


    const [teacherMark, setTeacherMark] = useState(
    submission.teacher_mark ??
    submission.suggested_mark ??
    0
 );

    const [saving, setSaving] = useState(false)

    async function saveMark(){
        setSaving(true)

        await fetch(`${process.env.NEXT_PUBLIC_API_URL}/submissions/${submission.id}`,{
            method:"PATCH",
            headers:{
                "Content-Type":"application/json",
            },
            body:JSON.stringify({teacher_mark:teacherMark})
        })
        router.push(`/scan/${submission.question_id}`)
    }
    

    return(
        <div className='space-y-6'>
            <div>
                <h2 className='font-semibold'>Teacher Mark</h2>

                <input
                    type='number'
                    value={teacherMark}
                    min={"0"}
                    max={"100"}
                    onChange={(e)=>setTeacherMark(e.target.value)}
                    className='mt-2 w-full rounded border p-3'
                />
            </div>

            <button
                onClick={saveMark}
                disabled={saving}
                className='rounded bg-blue-600 px-5 py-3 text-white disabled:opacity-50'
            >
                {saving? "saving ...":"Save Final Mark"}
            </button>
        </div>
    )
}