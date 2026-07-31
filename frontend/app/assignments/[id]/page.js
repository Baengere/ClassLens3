import Link from "next/link"


export default async function AssignmentPage({params}){
    const {id} = await params;
    console.log(id)
    const assignmentResponse = await fetch(`
        ${process.env.NEXT_PUBLIC_API_URL}/assignments/${id}`,
    {cache:"no-store"})

    const assignment = await assignmentResponse.json()

    const questionsResponse = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/questions/${id}`, {cache:"no-store"})

    const questions = await questionsResponse.json()
    

    return (
        <main className="max-w-3xl mx-auto p-8">
            <h1 className="text-3xl font-bold">{assignment.title}</h1>

            <p className="text-gray-600 mt-2">{assignment.subject}</p>

            {assignment.description && (
                <p className="mt-4">{assignment.description}</p>
            )}

            <hr className="my-8"/>

            <div className="flex items-center justify-between mb-4">
        
                <h2 className="text-2xl font-semibold">
                    Questions to mark
                </h2>

                <Link
                    href={`/assignments/${id}/questions/new`}
                    className="rounded bg-green-600 px-4 py-2 text-white hover:bg-green-700"
                >
                    + Add Question
                </Link>
            </div>

            

            {questions.length === 0 ? (
                <p>No questions yet.</p>
            ):(
                <ul className="space-y-4">{questions.map((question)=>(
                    <li key={question.id}className="border rounded-lg p-4">
                        <p className="font-medium">{question.question_text}</p>
                        <p className="text-sm text-gray-500 mt-2">
                            {question.marks} marks
                        </p>

                        <Link href={`/scan/${question.id}`}
                        className="inline-block mt-4 rounded bg-blue-600 px-4 py-2 text-white hover:bg-blue-700" 
                        > 📷 Scan Student Answer</Link>
                    </li>
                ))}</ul>
            )}
        </main>
    )
}