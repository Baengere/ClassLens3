import AssignmentForm from "./components/AssignmentForm"
import Link from "next/link";



export default async function Home(){
  const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/assignments/`,{
    cache: "no-store",
  });

  const assignments = await response.json()

  return (
    <main className="max-w-3xl mx-auto p-8">
      <h1 className="text-3xl font-bold mb-6">ClassLens3</h1>

      <AssignmentForm/>
      
      <h2 className="text-xl font-semibold mb-4"> My Assignments</h2>

      {assignments.length === 0 ? (
        <p>No assignments yet.</p>
      ):(
        <ul className="space-y-3">
          {assignments.map((assignment)=>(
            <li key={assignment.id} className="border rounded-lg p-4">
              <h3 className="font-semibold">{assignment.title}</h3>
              <p>{assignment.subject}</p>
              {assignment.description && (
                <p className="text-gray-500">{assignment.description}</p>
              )}
              <Link
                href={`/assignments/${assignment.id}`}
                className="inline-block mt-3 rounded bg-blue-600 px-4 py-2 text-white hover:bg-blue-700"
              >Open</Link>
            </li>
          ))}
        </ul>
      )}
    </main>
  )
}