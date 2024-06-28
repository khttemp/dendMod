private void OutPutAutoSaveFile(string path)
{
	StreamWriter streamWriter = File.CreateText(path);
	string text = "TrainCnt:\t" + this.mTrainOrg.Length;
	streamWriter.WriteLine(text);
	for (int i = 0; i < this.mTrainOrg.Length; i++)
	{
		int org = (int)this.mTrainOrg[i].mBtlTrain.OrgInfo.Org;
		int controll = (int)this.mTrainOrg[i].mBtlTrain.m_Controll;
		text = "Org" + i.ToString() + ":\t" + org.ToString();
		streamWriter.WriteLine(text);
		text = "Controll" + i.ToString() + ":\t" + controll.ToString();
		streamWriter.WriteLine(text);
		RailPos railPos = this.mTrainOrg[i].GetTopTrainBody().pTrack(0).FrontWheel.GetRailPos(0f);
		int railIndex = railPos.r.Parent.RailIndex;
		int boneNo = railPos.r.BoneNo;
		text = string.Concat(new string[]
		{
			"RailPos",
			i.ToString(),
			":\t",
			railIndex.ToString(),
			"\t",
			boneNo.ToString(),
			"\t",
			railPos.p.ToString()
		});
		streamWriter.WriteLine(text);
		float add = this.mTrainOrg[i].mBtlTrain.GetAdd();
		float addPer = this.mTrainOrg[i].mBtlTrain.GetAddPer();
		text = string.Concat(new string[]
		{
			"Speed",
			i.ToString(),
			":\t",
			add.ToString(),
			"\t",
			addPer.ToString()
		});
		streamWriter.WriteLine(text);
		text = string.Concat(new object[]
		{
			"Dir",
			i.ToString(),
			":\t",
			this.mTrainOrg[i].Dir
		});
		streamWriter.WriteLine(text);
		streamWriter.WriteLine("\n");
	}
	string str = "CPU:\t";
	if (this.mControll.mCPURoot.mCPUTrain != null)
	{
		int cpu = (int)this.mControll.mCPURoot.mCPUTrain.mBtlTrain.m_CPUProc.m_CPU;
		text = str + cpu.ToString();
		streamWriter.WriteLine(text);
		text = "CPUParam:\t" + this.mControll.mCPURoot.mCPUTrain.mBtlTrain.m_CPUProc.param.Length.ToString();
		for (int j = 0; j < this.mControll.mCPURoot.mCPUTrain.mBtlTrain.m_CPUProc.param.Length; j++)
		{
			text += "\t";
			text += this.mControll.mCPURoot.mCPUTrain.mBtlTrain.m_CPUProc.param[j].ToString();
		}
		streamWriter.WriteLine(text);
	}
	text = "ComicScript:\t" + this.chk_event_no.ToString();
	streamWriter.WriteLine(text);
	text = "CPUEvent:\t" + this.chk_cpu_no.ToString();
	streamWriter.WriteLine(text);
	text = "RainEvent:\t" + this.rain_no.ToString();
	streamWriter.WriteLine(text);
	text = "RailCnt:\t" + SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.RailList.Length.ToString();
	streamWriter.WriteLine(text);
	for (int k = 0; k < SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.RailList.Length; k++)
	{
		rail_list rail_list = SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.RailList[k];
		text = string.Concat(new string[]
		{
			k.ToString(),
			"\t",
			rail_list.prev_rail.ToString(),
			"\t",
			rail_list.block.ToString(),
			"\t",
			rail_list.offsetpos.x.ToString(),
			"\t",
			rail_list.offsetpos.y.ToString(),
			"\t",
			rail_list.offsetpos.z.ToString(),
			"\t",
			rail_list.dir.x.ToString(),
			"\t",
			rail_list.dir.y.ToString(),
			"\t",
			rail_list.dir.z.ToString(),
			"\t",
			rail_list.mdl_no.ToString(),
			"\t",
			rail_list.kasenchu_mdl_no.ToString(),
			"\t",
			rail_list.per.ToString(),
			"\t",
			((ulong)rail_list.flg & 255UL).ToString(),
			"\t",
			((ulong)(rail_list.flg >> 8) & 255UL).ToString(),
			"\t",
			((ulong)(rail_list.flg >> 16) & 255UL).ToString(),
			"\t",
			((ulong)(rail_list.flg >> 24) & 255UL).ToString(),
			"\t",
			rail_list.r.Length.ToString(),
			"\t"
		});
		for (int l = 0; l < rail_list.r.Length; l++)
		{
			text = string.Concat(new string[]
			{
				text,
				rail_list.r[l].next.rail.ToString(),
				"\t",
				rail_list.r[l].next.no.ToString(),
				"\t",
				rail_list.r[l].prev.rail.ToString(),
				"\t",
				rail_list.r[l].prev.no.ToString(),
				"\t"
			});
		}
		streamWriter.WriteLine(text);
	}
	text = "\nAmbCnt:\t" + SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.AmbList.Length.ToString() + "\t1";
	streamWriter.WriteLine(text);
	for (int num5 = 0; num5 < SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.AmbList.Length; num5++)
	{
		amb_list amb_list = SingletonMonoBehaviour<cGameMgr>.Instance.mStageTblMgr.AmbList[num5];
		text = string.Concat(new string[]
		{
			num5.ToString(),
			"\t",
			amb_list.rail_no.ToString(),
			"\t",
			amb_list.length.ToString(),
			"\t",
			amb_list.datalist.Count.ToString(),
			"\t"
		});
		for (int num6 = 0; num6 < amb_list.datalist.Count; num6++)
		{
			text = string.Concat(new string[]
			{
				text,
				amb_list.datalist[num6].mdl_no.ToString(),
				"\t",
				amb_list.datalist[num6].parentindex.ToString(),
				"\t",
				amb_list.datalist[num6].offsetpos.x.ToString(),
				"\t",
				amb_list.datalist[num6].offsetpos.y.ToString(),
				"\t",
				amb_list.datalist[num6].offsetpos.z.ToString(),
				"\t",
				amb_list.datalist[num6].dir.x.ToString(),
				"\t",
				amb_list.datalist[num6].dir.y.ToString(),
				"\t",
				amb_list.datalist[num6].dir.z.ToString(),
				"\t",
				amb_list.datalist[num6].joint_dir.x.ToString(),
				"\t",
				amb_list.datalist[num6].joint_dir.y.ToString(),
				"\t",
				amb_list.datalist[num6].joint_dir.z.ToString(),
				"\t",
				amb_list.datalist[num6].per.ToString(),
				"\t",
				amb_list.datalist[num6].size_per.ToString(),
				"\t"
			});
		}
		streamWriter.WriteLine(text);
	}
	streamWriter.Flush();
	streamWriter.Close();
}