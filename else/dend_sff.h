static const Sint32 CHARA_CODE_MAX	= 9362;
static const Sint32 SHEET_MAX		= 256;

struct SFFHEADER
{
	Uint32 Guid;
	Uint8 FontSize;
	Uint8 SheetMax;
	Uint16 FontMax;
	Uint16 IndexTbl[CHARA_CODE_MAX];
};

struct SheetName
{
    char Name[32];
}

struct SFontSheetData
{
    Uint64 SheetNo	: 8;
    Uint64 Left		: 6;
    Uint64 Right	: 6;
    Uint64 x1		: 11;
    Uint64 y1		: 11;
    Uint64 x2		: 11;
    Uint64 y2		: 11;
};