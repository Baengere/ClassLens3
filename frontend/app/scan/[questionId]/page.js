import ScanForm from "./ScanForm";

export default async function ScanPage({ params }) {
    const { questionId } = await params;

    const response = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/questions/detail/${questionId}`,
        {
            cache: "no-store",
        }
    );

    const question = await response.json();

    return (
        <main className="max-w-3xl mx-auto p-8 ">

            <h1 className="text-3xl font-bold bg-black p-2">
                Scan Student Paper
            </h1>

            <div className="mt-6 rounded-lg border p-4 bg-gray-400">

                <h2 className="text-xl font-semibold">
                    Question
                </h2>

                <p className="mt-2">
                    {question.question_text}
                </p>

                <p className="mt-4 font-medium">
                    Total Marks: {question.marks}
                </p>

            </div>

            <div className="mt-8">
                <ScanForm questionId={questionId} />
            </div>

        </main>
    );
}