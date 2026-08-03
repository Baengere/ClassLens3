import AssignmentForm from "./components/forms/AssignmentForm";
import Link from "next/link";
import AppHeader from "./components/layout/AppHeader";
import PageContainer from "./components/layout/PageContainer";
import HeroCard from "./components/dashboard/HeroCard";
import Card from "./components/ui/Card";
import SectionTitle from "./components/ui/SectionTitle";


export default async function Home() {
  
  const response = await fetch(
    `${process.env.NEXT_PUBLIC_API_URL}/assignments/`,
    {
      cache: "no-store",
    }
  );

  const assignments = await response.json();

  return(

    <PageContainer>

      <AppHeader/>

      <HeroCard assignment={assignments[0]}/>

      <SectionTitle>
        Recent Assignments
      </SectionTitle>

      {assignments.length === 0 ? (
        <Card>
          <p className="text-slate-500 text-center">
            No assignments yet.
          </p>
        </Card>
      ):(
        <div className="space-y-5 mb-10">

          {assignments.map((assignment)=>(

            <Card key={assignment.id}>

              <div className="flex items-center justify-between">

                <div>

                  <h3 className="text-xl font-semibold">
                    {assignment.title}
                  </h3>

                  <p className="mt-1 text-slate-500">
                    {assignment.subject}
                  </p>

                  {assignment.description && (
                    <p className="mt-3 text-slate-600">
                      {assignment.description}
                    </p>
                  )}

                </div>

                <Link href={`/assignments/${assignment.id}`}
                  className="rounded-xl bg-blue-600 px-5 py-3 text-white hover:bg-blue-700">
                    Open
                </Link>

              </div>

            </Card>

          ))}

        </div>

      )}

      <Card>

        <SectionTitle>
          Create New Assignment
        </SectionTitle>

        <AssignmentForm/>

      </Card>

    </PageContainer>
  )
}