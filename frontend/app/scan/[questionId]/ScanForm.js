"use client"
import {useRouter} from 'next/navigation'
import {useState} from 'react'

export default function ScanForm({questionId}){
    const router = useRouter()

    const[image, setImage] = useState(null);
    const [loading, setLoading] = useState(false)

    async function handleSubmit(e){
        e.preventDefault();

        const formData = new FormData()

        formData.append("question_id",questionId)
        formData.append("image", image)

        setLoading(true)

        const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/submissions/`,{
            method: "POST",
            body:formData,
        });

        setLoading(false)

        const submission = await response.json()

        router.push(`/submissions/${submission.id}`)
    }

    return(
        <form onSubmit={handleSubmit} className='space-y-8'>
            <label className='block cursor-pointer rounded-lg border-2 border-dashed p-10 text-center hover:bg-gray-50'>
                <p className="text-4xl">📷</p>

                <p className='mt-4'>Choose a student paper</p>

                <input
                    hidden
                    type='file'
                    accept='image'
                    onChange={(e)=>setImage(e.target.files[0])}
                />

            </label>
            <button disabled={loading} className='rounded bg-blue-600 px-5 py-3 text-white'>
                {loading? "Uploading...":"Upload"}
            </button>
        </form>
    )
}