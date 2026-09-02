VALID_STATUSES = {
    "Aktif",
    "Bakımda",
    "Pasif"
}

VALID_DEVICE_TYPES = {
    "Masaüstü Bilgisayar",
    "Dizüstü Bilgisayar",
    "Yazıcı",
    "Monitör"
}


assets = [
    {
        "inventory_no": "ENV-001",
        "device_name": "PC-MH-01",
        "device_type": "Masaüstü Bilgisayar",
        "department": "Mali Hizmetler",
        "status": "Aktif"
    },
    {
        "inventory_no": "ENV-002",
        "device_name": "NB-IK-02",
        "device_type": "Dizüstü Bilgisayar",
        "department": "İnsan Kaynakları",
        "status": "Aktif"
    },
    {
        "inventory_no": "ENV-003",
        "device_name": "PR-ID-01",
        "device_type": "Yazıcı",
        "department": "İdari İşler",
        "status": "Bakımda"
    },
    {
        "inventory_no": "ENV-003",
        "device_name": "PR-BI-02",
        "device_type": "Yazıcı",
        "department": "Bilgi İşlem",
        "status": "Aktif"
    },
    {
        "inventory_no": "",
        "device_name": "PC-TH-04",
        "device_type": "Masaüstü Bilgisayar",
        "department": "Teknik Hizmetler",
        "status": "Aktif"
    },
    {
        "inventory_no": "ENV-006",
        "device_name": "",
        "device_type": "Tablet",
        "department": "Mali Hizmetler",
        "status": "Hazır"
    }
]


def validate_required_fields(asset):
    required_fields = [
        "inventory_no",
        "device_name",
        "device_type",
        "department",
        "status"
    ]

    missing_fields = []

    for field in required_fields:
        if not asset.get(field):
            missing_fields.append(field)

    return missing_fields


def validate_device_type(asset):
    return (
        asset["device_type"]
        in VALID_DEVICE_TYPES
    )


def validate_status(asset):
    return (
        asset["status"]
        in VALID_STATUSES
    )
def find_duplicate_inventory_numbers(asset_list):
    inventory_counts = {}

    for asset in asset_list:
        inventory_no = asset.get("inventory_no")

        if not inventory_no:
            continue

        if inventory_no not in inventory_counts:
            inventory_counts[inventory_no] = 0

        inventory_counts[inventory_no] += 1

    duplicates = []

    for inventory_no, count in inventory_counts.items():
        if count > 1:
            duplicates.append(inventory_no)

    return duplicates


def audit_asset(asset, duplicate_numbers):
    problems = []

    missing_fields = validate_required_fields(asset)

    if missing_fields:
        problems.append(
            "Missing fields: "
            + ", ".join(missing_fields)
        )

    if asset.get("device_type"):
        if not validate_device_type(asset):
            problems.append(
                "Invalid device type: "
                + asset["device_type"]
            )

    if asset.get("status"):
        if not validate_status(asset):
            problems.append(
                "Invalid status: "
                + asset["status"]
            )

    inventory_no = asset.get("inventory_no")

    if inventory_no in duplicate_numbers:
        problems.append(
            "Duplicate inventory number: "
            + inventory_no
        )

    return problems

duplicate_numbers = find_duplicate_inventory_numbers(assets)

audit_results = []

for asset in assets:
    problems = audit_asset(asset, duplicate_numbers)

    audit_results.append({
        "inventory_no": asset.get("inventory_no"),
        "device_name": asset.get("device_name"),
        "problems": problems
    })

total_assets = len(audit_results)

valid_assets = sum(
    1 for result in audit_results
    if len(result["problems"]) == 0
)

problem_assets = total_assets - valid_assets

print()
print("ASSET INVENTORY AUDIT REPORT")
print("=" * 60)

print(f"Total Assets   : {total_assets}")
print(f"Valid Assets   : {valid_assets}")
print(f"Problem Assets : {problem_assets}")

print()
print("AUDIT DETAILS")
print("-" * 60)

for result in audit_results:

    if result["problems"]:
        print(
            f"{result['inventory_no']} - "
            f"{result['device_name']}"
        )

        for problem in result["problems"]:
            print(f"  - {problem}")

    else:
        print(
            f"{result['inventory_no']} - "
            f"{result['device_name']} : OK"
        )

print("=" * 60)