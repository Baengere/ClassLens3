import Link from 'next/link';
import Card from '../ui/Card'

export default function HeroCard({assignment}){
    if(!assignment) return null;

    return(
        <Card className="mb-10 bg-gradient-to-r from-blue-600 to-indigo-600 text-white border-0 shadow-xl">
            <p className="uppercase tracking-widest text-sm text-blue-100">
                Continue Marking
            </p>

            <h2 className="mt-3 text-3xl font-bold">{assignment.title}</h2>

            <Link
                href={`/assignment/${assignment.id}`}
                className="mt-8 inline-block rounded-xl bg-white px-6 py-3 font-semiblod text-blue-600"
            >
                Continue →
            </Link>

        </Card>
    )
}