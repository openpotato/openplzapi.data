import csv
import sys

def diff_csv(osm_file, del_file, diff_file):
    
    # Read the del_file into a set of rows for fast lookup
    with open(del_file, mode='r', newline='', encoding="UTF8") as del_stream:
        del_reader = csv.reader(del_stream, delimiter=',')
        del_rows = {tuple(row) for row in del_reader}

    # Open the osm_file and diff_file
    with open(osm_file, mode='r', newline='', encoding="UTF8") as osm_stream, open(diff_file, mode='w', newline='', encoding="UTF8") as diff_stream:
        osm_reader = csv.reader(osm_stream, delimiter=',')
        diff_writer = csv.writer(diff_stream, delimiter=',', lineterminator='\n')

        # Get header from osm_file and write it to diff_file
        osm_header = next(osm_reader)
        diff_writer.writerow(osm_header)

        # Iterate through the rows in osm_file and write only those not in del_file
        for osm_row in osm_reader:
            if tuple(osm_row) not in del_rows:
                diff_writer.writerow(osm_row)

    print(f"Diff written to {diff_file}")

if __name__ == "__main__":
    
    if len(sys.argv) != 4:
        print("Usage: python diff.py <osm_file> <del_file> <diff_file>")
    else:
        diff_csv(sys.argv[1], sys.argv[2], sys.argv[3])     
