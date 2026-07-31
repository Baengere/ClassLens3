import QuestionForm from './QuestionForm'

export default async function NewQuestionPage({params}){
    const {id} = await params;

    return(
        <main className='max-w-3xl mx-auto p-8'>
            <h1 className='text-3xl font-bold mb-6'>New Question</h1>

            <QuestionForm assignmentId={id}/>
        </main>
    )
}