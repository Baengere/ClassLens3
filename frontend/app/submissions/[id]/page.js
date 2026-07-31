import ReviewPanel from "./ReviewPanel";
import Link from "next/link";

export default async function SubmissionPage({params}){

    const {id} = await params;

    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/submissions/detail/${id}`,
        {
            cache: "no-store"
        }
    );
    const submission = await response.json();

    return(
        <main className = "max-w-3xl mx-auto p-8">
            <h1 className="text-3xl font-semibold mb-6">
                Review Submission
            </h1>

            <div className="space-y-6">
                <div>
                    <h2 className="font-semibold">OCR Text</h2>
                    <p className="border rounded p-4 mt-2 whitespace-pre-wrap">
                        {submission.ocr_text || "No OCR Text"}
                    </p>
                    <img
                        src={`${process.env.NEXT_PUBLIC_API_URL}/${submission.image_path}`}
                        alt="Student Paper"
                        className="w-full rounded-lg border"
                    />
                </div>

                <div>
                    <h2 className="font-semibold">
                        Suggested Mark
                    </h2>
                    <p className="mt-2">{submission.suggested_mark ?? "-"}</p>
                    <ReviewPanel submission={submission}/>
                </div>

                <div>
                    <h2 className="font-semibold">Status</h2>
                    <p className="mt-2">{submission.status}</p>
                </div>
                <div className="mt-8">
                    <Link
                        href={`/scan/${submission.question.id}`}
                        className="inline-block rounded bg-green-600 px-5 py-3 text-white hover:bg-green-700"
                    >
                         📷 Scan Another Page
                    </Link>
                </div>
            </div>
        </main>
    )


}